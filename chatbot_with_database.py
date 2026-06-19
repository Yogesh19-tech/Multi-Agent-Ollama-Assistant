import streamlit as st
import mysql.connector
import subprocess
import pandas as pd

# -------------------------
# DB Connection
# -------------------------
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",  # plain string, no quote_plus
        database="classicmodels"
    )

# -------------------------
# Ollama Helper
# -------------------------
def run_ollama(model: str, prompt: str) -> str:
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt,
        text=True,
        capture_output=True
    )
    return result.stdout.strip()

# -------------------------
# SQL Agent
# -------------------------
def ask_sql_agent(question: str, schema_text: str) -> str:
    prompt = f"""
    You are an expert MySQL assistant.
    Schema:
    {schema_text}

    Question: {question}

    Generate ONLY a valid MySQL query (no explanations).
    """
    return run_ollama("llama3", prompt)

# -------------------------
# General Chat Agent
# -------------------------
def ask_chat_agent(question: str) -> str:
    prompt = f"""
    You are a helpful AI assistant.
    User: {question}
    Answer in a clear, conversational way.
    """
    return run_ollama("llama3", prompt)

# -------------------------
# Cleanup Helper
# -------------------------
def clean_query(raw_query: str) -> str:
    q = raw_query.strip()

    # Remove Markdown code fences and language hints
    q = q.replace("```sql", "").replace("```", "")

    # Remove any wrapping triple quotes
    if (q.startswith("'''") and q.endswith("'''")) or (q.startswith('"""') and q.endswith('"""')):
        q = q[3:-3].strip()

    # Remove wrapping backticks, single or double quotes
    q = q.strip("`").strip("'").strip('"')

    # Remove trailing semicolon if present
    if q.endswith(";"):
        q = q[:-1]

    return q.strip()

# -------------------------
# Streamlit UI
# -------------------------
st.set_page_config(page_title="Multi-Agent Ollama Assistant", layout="wide")

st.title("🦙 Multi-Agent Ollama Assistant")
st.write("Choose between **SQL Agent** and **General Chat Agent**")

# Schema (hardcoded for demo; could be auto-fetched)
schema_text = """
Tables and Columns:

customers(customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit)
orders(orderNumber, orderDate, requiredDate, shippedDate, status, comments, customerNumber)
orderdetails(orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber)
products(productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP)
productlines(productLine, textDescription, htmlDescription, image)
payments(customerNumber, checkNumber, paymentDate, amount)
employees(employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle)
offices(officeCode, city, phone, addressLine1, addressLine2, state, country, postalCode, territory)
"""

# Sidebar Agent Selection
agent_choice = st.sidebar.radio("🤖 Select Agent:", ["SQL Agent", "General Chat Agent"])

# Input
question = st.text_input("💬 Ask a question:")

if question:
    if agent_choice == "SQL Agent":
        with st.spinner("🦙 Thinking (SQL Agent)..."):
            raw_sql_query = ask_sql_agent(question, schema_text)
            sql_query = clean_query(raw_sql_query)

            st.subheader("Generated SQL Query")
            st.code(sql_query, language="sql")

            try:
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute(sql_query)
                rows = cursor.fetchall()
                col_names = [desc[0] for desc in cursor.description]

                df = pd.DataFrame(rows, columns=col_names)
                st.success("✅ Query executed successfully!")
                st.dataframe(df)

                conn.close()
            except Exception as e:
                st.error(f"❌ Error executing query: {e}")

    elif agent_choice == "General Chat Agent":
        with st.spinner("🦙 Thinking (Chat Agent)..."):
            answer = ask_chat_agent(question)
            st.subheader("Assistant's Reply")
            st.write(answer)