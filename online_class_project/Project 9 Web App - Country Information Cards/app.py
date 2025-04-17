import streamlit as st
import requests

st.set_page_config(page_title="Country Info Cards", layout="wide")

st.title("🌍 Country Information Cards")

# Inject custom CSS for animations
st.markdown("""
    <style>
    @keyframes fadeInUp {
        0% {
            opacity: 0;
            transform: translateY(20px);
        }
        100% {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        margin: 10px 0;
        animation: fadeInUp 0.5s ease forwards;
        transition: transform 0.2s;
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 14px rgba(0,0,0,0.15);
    }

    </style>
""", unsafe_allow_html=True)


# Search bar
search_query = st.text_input("🔍 Search for a country (or leave blank to show all):")

# Fetch country data
@st.cache_data
def get_countries():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
         st.error("Failed to load country data.")
    return []

countries = get_countries()

# Filter based on search
if search_query:
    countries = [c for c in countries if search_query.lower() in c.get("name", {}).get("common", "").lower()]
# Show in columns (3 per row)
cols_per_row = 3
for idx, country in enumerate(countries):
    col = st.columns(cols_per_row)[idx % cols_per_row]
    with col:
        flag = country.get("flags", {}).get("png", "")
        name = country.get("name", {}).get("common", "Unknown")
        capital = country.get("capital", ["N/A"])[0]
        region = country.get("region", "N/A")
        population = f"{country.get('population', 'N/A'):,}"

        languages = ", ".join(country.get("languages", {}).values()) if country.get("languages") else "N/A"

        currencies = country.get("currencies", {})
        currency_names = ", ".join(
            [f"{v.get('name')} ({v.get('symbol')})" for v in currencies.values()]
        ) if currencies else "N/A"

        # Inject full card as HTML with fadeInUp animation
        html_content = f"""
        <div class="card" style="animation-delay: {idx * 0.1}s;">
            <img src="{flag}" style="width: 100%; max-width: 150px; border-radius: 8px;" />
            <h3>{name}</h3>
            <p><strong>Capital:</strong> {capital}</p>
            <p><strong>Region:</strong> {region}</p>
            <p><strong>Population:</strong> {population}</p>
            <p><strong>Languages:</strong> {languages}</p>
            <p><strong>Currency:</strong> {currency_names}</p>
        </div>
        """
        st.markdown(html_content, unsafe_allow_html=True)
