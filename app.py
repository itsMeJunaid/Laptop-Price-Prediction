import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load('Model/laptop_price_model.pkl')

# Define the Streamlit app
st.image("lap.png", use_column_width=True)
st.title('Laptop Price Prediction 💻')
st.write("Created By [Muhammad Junaid](https://itsmejunaid.github.io/).", unsafe_allow_html=True)

# Add custom CSS
st.markdown("""
    <style>
        .custom-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
            margin: auto;
            padding: 20px;
            background-color: #red;
            border: 1px solid #ccc;
            border-radius: 50px;
        }
        .left-column, .right-column {
            flex: 1;
            
        }
        .left-column {
            border-right: 1px solid #ccc;
            padding-right: 20px;
        }
        .right-column {
            padding-left: 20px;
        }
        .app-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 20px;
        }
        .app-header img {
            height: 80px;
            width: auto;
        }
    </style>
    """, unsafe_allow_html=True)

st.write("""
### Enter the details of the laptop:
""")

# User inputs
company = st.selectbox('Company', ['Apple', 'HP', 'Dell', 'Lenovo', 'Asus', 'Acer', 'MSI', 'Microsoft'])
type_name = st.selectbox('Type', ['Ultrabook', 'Notebook', 'Gaming', '2 in 1 Convertible','Latitude'])
inches = st.number_input('Screen Size (inches)', min_value=10.0, max_value=18.0, value=15.6)
screen_resolution = st.text_input('Screen Resolution', 'Full HD 1920x1080')
ram = st.text_input('RAM (GB)', '8GB')
memory = st.text_input('Memory', '256GB SSD')
gpu = st.text_input('GPU', 'Intel HD Graphics 620')
op_sys = st.selectbox('Operating System', ['Windows 10', 'macOS', 'Linux', 'No OS'])
weight = st.number_input('Weight (kg)', min_value=0.5, max_value=5.0, value=2.0)
cpu = st.text_input('Cpu', 'Intel Core i5 2.3GHz')

# Create a button to predict the price
if st.button('Predict Price'):
    # Create dataframe from inputs
    user_input = {
        'Company': [company],
        'TypeName': [type_name],
        'Inches': [inches],
        'ScreenResolution': [screen_resolution],
        'Ram': [ram],
        'Memory': [memory],
        'Gpu': [gpu],
        'OpSys': [op_sys],
        'Weight': [weight],
        'Cpu': [cpu]
    }

    new_data = pd.DataFrame(user_input)

    # Clean new data
    new_data['Weight'] = new_data['Weight'].astype(float)
    new_data['Ram'] = new_data['Ram'].str.replace('GB', '').astype(int)
    new_data['Cpu_GHz'] = new_data['Cpu'].apply(lambda x: float(x.split()[-1][:-3]))

    # Predict the price
    predicted_price_eur = model.predict(new_data)
    predicted_price_pkr = predicted_price_eur * 297.79

    # Display the specifications and price in a custom container
    st.markdown(f"""
        <div class="custom-container">
            <div class="left-column">
                <h3>Your Laptop Specifications🔊:</h3>
                <p><strong>Company:</strong> {company}</p>
                <p><strong>Type:</strong> {type_name}</p>
                <p><strong>Screen Size:</strong> {inches} inches</p>
                <p><strong>Screen Resolution:</strong> {screen_resolution}</p>
                <p><strong>RAM:</strong> {ram}</p>
                <p><strong>Memory:</strong> {memory}</p>
                <p><strong>GPU:</strong> {gpu}</p>
                <p><strong>Operating System:</strong> {op_sys}</p>
                <p><strong>Weight:</strong> {weight} kg</p>
                <p><strong>CPU:</strong> {cpu}</p>
            </div>
            <div class="right-column">
                <h1>Predicted Price 💵:</h1>
                <p><h2>{predicted_price_eur[0]:.2f} EUR</h2></p>
                <p><h2>{predicted_price_pkr[0]:.2f} PKR</h2></p>
            </div>
        </div>
        """, unsafe_allow_html=True)

else:
    st.write("Please enter all the details and click the 'Predict Price' button to get the predicted price.")
    st.write('This App is Developed By [Muhammad Junaid](https://itsmejunaid.github.io/).', unsafe_allow_html=True)
