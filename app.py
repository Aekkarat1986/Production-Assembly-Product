import streamlit as st
import pandas as pd
from datetime import datetime

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="Jozu Auto Part - Production Control", page_icon="🏭", layout="wide")

st.title("🏭 Jozu Auto Part: Process Data Entry System")
st.markdown("---")

# เลือกกระบวนการผลิตที่ต้องการบันทึกข้อมูล
process_choice = st.sidebar.selectbox("เลือกขั้นตอนการผลิต (Process)", [
    "1. Press Process", 
    "2. ส่งชุบ (Plating Out)", 
    "3. Stock ชุบ & รับชุบ (Plating In)", 
    "4. Stock Component", 
    "5. Assembly (Ass'y)", 
    "6. Stock Cap Comp & Delivery"
])

# ---------------------------------------------------------
# 1. กระบวนการ Press
# ---------------------------------------------------------
if process_choice == "1. Press Process":
    st.header("⚙️ บันทึกข้อมูลกระบวนการ Press")
    with st.form("form_press"):
        date_val = st.date_input("วันที่", datetime.now())
        qty = st.number_input("จำนวน", min_value=1, value=100)
        lot = st.text_input("Lot No.")
        p_no = st.selectbox("P/No (Part Number)", [
            "J0701-17620-Z1T-8000-20", 
            "J0701-17620-Z1T-8000-21", 
            "J0701-17620-Z1T-8000-23", 
            "J0701-17620-Z1T-8000-25"
        ])
        p_name = st.text_input("PName (ชื่อชิ้นส่วน เช่น CAP, OUTER)")
        operator = st.text_input("ชื่อพนักงาน")
        qc = st.selectbox("QC Status", ["Pass", "Fail"])
        mat_size = st.text_input("ขนาด mat")
        
        submitted = st.form_submit_button("💾 บันทึกข้อมูล Press")
        if submitted:
            st.success(f"บันทึกข้อมูล Press ของ Part {p_no} (Lot: {lot}) เรียบร้อย!")

# ---------------------------------------------------------
# 2. กระบวนการ ส่งชุบ
# ---------------------------------------------------------
elif process_choice == "2. ส่งชุบ (Plating Out)":
    st.header("🚚 บันทึกข้อมูลส่งชุบ")
    with st.form("form_plating_out"):
        date_val = st.date_input("วันที่", datetime.now())
        qty = st.number_input("จำนวน", min_value=1, value=100)
        lot = st.text_input("Lot No.")
        p_no = st.text_input("P/No")
        p_name = st.text_input("PName")
        operator = st.text_input("ผู้ผลิต")
        plating_type = st.selectbox("ชนิดการชุบ", ["TEP or BC", "TPI or APK", "TI ADT"])
        log_no = st.text_input("Log. No.")
        
        submitted = st.form_submit_button("💾 บันทึกข้อมูลส่งชุบ")
        if submitted:
            st.success(f"บันทึกข้อมูลส่งชุบ (Log: {log_no}) เรียบร้อย!")

# ---------------------------------------------------------
# 3. กระบวนการ Stock ชุบ & รับชุบ
# ---------------------------------------------------------
elif process_choice == "3. Stock ชุบ & รับชุบ (Plating In)":
    st.header("📦 บันทึกข้อมูล Stock ชุบ / รับชุบ")
    with st.form("form_plating_in"):
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("ส่วน Stock ชุบ")
            stock_remain = st.text_input("เหลือเท่าไร")
            stock_where = st.text_input("ที่ไหน")
        with col2:
            st.subheader("ส่วนรับชุบ")
            date_val = st.date_input("วันที่รับ", datetime.now())
            qty = st.number_input("จำนวนรับ", min_value=1, value=100)
            lot = st.text_input("Lot No.")
            p_no = st.text_input("P/No")
            p_name = st.text_input("PName")
            operator = st.text_input("ผู้ผลิต")
            plating_type = st.text_input("ชนิดการชุบ")
            log_no = st.text_input("Log. No.")
            
        submitted = st.form_submit_button("💾 บันทึกข้อมูล Stock/รับชุบ")
        if submitted:
            st.success("บันทึกข้อมูลรับชุบเรียบร้อย!")

# ---------------------------------------------------------
# 4. กระบวนการ Stock Component
# ---------------------------------------------------------
elif process_choice == "4. Stock Component":
    st.header("🗄️ ตรวจสอบ / บันทึก Stock Component")
    st.markdown("รายการชิ้นส่วนประกอบทั้งหมดในสต็อก:")
    
    comp_df = pd.DataFrame({
        "Part No": [
            "J0701-17620-Z1T-8000-20", "J0701-17620-Z1T-8000-21", 
            "J0701-17620-Z1T-8000-23", "J0701-17620-Z1T-8000-25",
            "J0701-17620-Z1T-8000-22", "J0701-17631-Z1T-8002", 
            "J0701-17620-Z1T-8000-24"
        ],
        "Part Name": [
            "CAP, OUTER", "CAP, INNER", "SPRING, PLATE", 
            "SEPARATOR, FUEL SUP", "SEPARATOR, FUEL (Sup.B)", 
            "PACKING, FUEL FILLER", "RIVET 3x4"
        ]
    })
    st.dataframe(comp_df, use_container_width=True)

# ---------------------------------------------------------
# 5. กระบวนการ Ass'y (Assembly)
# ---------------------------------------------------------
elif process_choice == "5. Assembly (Ass'y)":
    st.header("🛠️ บันทึกข้อมูลกระบวนการประกอบ (Ass'y)")
    st.info("โครงสร้างการประกอบ LV1 (17620-Z1T-8010 Cap Comp Fuel Filler)")
    
    with st.form("form_assy"):
        operator_assy = st.text_input("ชื่อพนักงานผู้ประกอบ")
        lot_assy = st.text_input("Lot ผลิตชิ้นงานสำเร็จรูป")
        qty_assy = st.number_input("จำนวนที่ประกอบได้ (Sets)", min_value=1, value=50)
        
        st.markdown("**ตรวจสอบรายการชิ้นส่วนประกอบ (LV2):**")
        chk1 = st.checkbox("ครบถ้วน: J0701-17620-Z1T-8000-20 (CAP, OUTER) - ใช้ 1")
        chk2 = st.checkbox("ครบถ้วน: J0701-17620-Z1T-8000-21 (CAP, INNER) - ใช้ 1")
        chk3 = st.checkbox("ครบถ้วน: J0701-17620-Z1T-8000-23 (SPRING, PLATE) - ใช้ 1")
        chk4 = st.checkbox("ครบถ้วน: J0701-17620-Z1T-8000-25 (SEPARATOR, FUEL SUP) - ใช้ 1")
        chk5 = st.checkbox("ครบถ้วน: J0701-17620-Z1T-8000-22 (SEPARATOR, FUEL Sup.B) - ใช้ 1")
        chk6 = st.checkbox("ครบถ้วน: J0701-17631-Z1T-8002 (PACKING, FUEL FILLER) - ใช้ 1")
        chk7 = st.checkbox("ครบถ้วน: J0701-17620-Z1T-8000-24 (RIVET 3x4) - ใช้ 2")
        
        submitted = st.form_submit_button("💾 ยืนยันการประกอบและบันทึกข้อมูล")
        if submitted:
            if chk1 and chk2 and chk3 and chk4 and chk5 and chk6 and chk7:
                st.success(f"ประกอบชิ้นงานสำเร็จ! บันทึก Lot: {lot_assy} เรียบร้อย")
            else:
                st.error("กรุณาตรวจสอบชิ้นส่วนส่วนประกอบ (LV2) ให้ครบทุกรายการก่อนบันทึก")

# ---------------------------------------------------------
# 6. กระบวนการ Stock Cap Comp & Delivery
# ---------------------------------------------------------
elif process_choice == "6. Stock Cap Comp & Delivery":
    st.header("🏁 บันทึกข้อมูลคลังสินค้าและจัดส่ง (Delivery)")
    with st.form("form_delivery"):
        date_del = st.date_input("วันที่จัดส่ง", datetime.now())
        product_no = st.text_input("Product No.", value="17620-Z1T-8010 Cap Comp Fuel Filler")
        delivery_qty = st.number_input("จำนวนจัดส่ง", min_value=1, value=100)
        destination = st.text_input("ลูกค้า / ปลายทางจัดส่ง")
        driver_name = st.text_input("ผู้ส่งมอบ / เจ้าหน้าที่")
        
        submitted = st.form_submit_button("💾 บันทึกข้อมูลจัดส่ง")
        if submitted:
            st.success(f"บันทึกข้อมูลจัดส่งสินค้า {product_no} จำนวน {delivery_qty} ชิ้น เรียบร้อย!")
