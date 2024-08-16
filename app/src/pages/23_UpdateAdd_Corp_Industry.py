import logging
logger = logging.getLogger(__name__)
import requests
import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.header('Update/Add a Company or Industry')

update_corp = st.button('Update Company')

add_corp = st.button("Add Company")

update_ind = st.button('Update Industry')

add_ind = st.button("Add Industry")



if update_corp:
    with st.form("Update Company"):
        companyID = st.number_input("Company ID", step =1, format = "%d")
        name = st.text_input("Company Name")
        num_emps = st.text_input("Number of Employees")
        founding_date = st.date_input("Founding Date")
        emp_benefits = st.text_area("Employee Benefits")
        value = st.number_input("Value of Company")
        ind_id = st.number_input("Industry ID", step = 1, format = "%d")

        update_company = st.form_submit_button("Update Company")
        if update_company:
            corp_info = {}
            corp_info["companyID"] = companyID
            corp_info["name"] = name
            corp_info["numEmployees"] = num_emps
            corp_info["foundingDate"] = founding_date
            corp_info["empBenefits"] = emp_benefits
            corp_info["value"] = value
            corp_info["indID"] = ind_id
            
            st.success("Company updated")
            requests.put(f'http://api:4000/co/company', json = corp_info)

if add_corp:
    with st.form("Add Company"):
        companyID = st.number_input("Company ID", step =1, format = "%d")
        name = st.text_input("Company Name")
        num_emps = st.text_input("Number of Employees")
        founding_date = st.date_input("Founding Date")
        emp_benefits = st.text_area("Employee Benefits")
        value = st.number_input("Value of Company")
        ind_id = st.number_input("Industry ID", step = 1, format = "%d")

        add_company = st.form_submit_button("Add Company")
        if add_company:
            corp_info = {}
            corp_info["companyID"] = companyID
            corp_info["name"] = name
            corp_info["numEmployees"] = num_emps
            corp_info["foundingDate"] = founding_date
            corp_info["empBenefits"] = emp_benefits
            corp_info["value"] = value
            corp_info["indID"] = ind_id
            
            st.success("Company added")
            requests.post(f'http://api:4000/co/company', json = corp_info)


if update_ind:
    with st.form("Update Industry"):
        indID = st.number_input("Industry ID", step =1, format = "%d")
        indName = st.text_input("Industry Name")
        indSize = st.text_input("Industry Size")

        update_industry = st.form_submit_button("Update Industry")
        
        if update_industry:
            ind_info = {}
            ind_info["indID"] = indID
            ind_info["name"] = indName
            ind_info["size"] = indSize
            st.success("Industry updated")
            requests.put(f'http://api:4000/i/industry', json = ind_info)

if add_ind:
    with st.form("Add Industry"):
        indID = st.number_input("Industry ID", step =1, format = "%d")
        indName = st.text_input("Industry Name")
        indSize = st.text_input("Industry Size")

        add_industry = st.form_submit_button("Add Industry")
        
        if add_industry:
            ind_info = {}
            ind_info["indID"] = indID
            ind_info["name"] = indName
            ind_info["size"] = indSize
            st.success("Industry added")
            requests.post(f'http://api:4000/i/industry', json = ind_info)