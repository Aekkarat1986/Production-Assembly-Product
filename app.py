import streamlit as st
import pandas as pd
from datetime import datetime

# ตั้งค่าหน้าเว็บแบบกว้าง
st.set_page_config(page_title="Jozu Auto Part - Production Control", page_icon="🏭", layout="wide")

st.title("🏭 Jozu Auto Part: Process Data Entry System")
st.markdown("---")
st.markdown("💡 **ระบบบันทึกข้อมูลทุกกระบวนการผลิต (แสดงหน้าจอเดียวทั้งหมด)**")

# ---------------------------------------------------------
# 1. กระบวนการ Press
# ---------------------------------------------------------
st.header("⚙️ 1. กระบวนการ Press")
with st.form("form_press"):
    col1, col2 = st.columns(2)
    with col1:
        date_val = st.date_input("วันที่ (Press)", datetime.now(), key="date_press")
        qty = st.number_input("จำนวน", min_value=1, value=100, key="qty_press")
        lot = st.text_input("Lot No.", key="lot_press")
    with col2:
        p_no = st.selectbox("P/No (Part Number)", [
            "J0701-17620-Z1T-8000-20", 
            "J0701-17620-Z1T-8000-21", 
            "J0701-17620-Z1T-8000-23", 
            "J0701-17620-Z1T-8000-25"
        ], key="pno_press")
        p_name = st.text_input("PName", value="CAP, OUTER", key="pname_press")
        operator = st.text_input("ชื่อพนักงาน (Press)", key="op_press")
        qc = st.selectbox("QC Status", ["Pass", "Fail"], key="qc_press")
        mat_size = st.text_input("ขนาด mat", key="mat_press")
    
    submitted_press = st.form_submit_button("💾 บันทึกข้อมูล Press")
    if submitted_press:
        st.success(f"บันทึกข้อมูล Press ของ Part {p_no} เรียบร้อย!")

st.markdown("---")

# ---------------------------------------------------------
# 2. กระบวนการ ส่งชุบ
# ---------------------------------------------------------
st.header("🚚 2. กระบวนการ ส่งชุบ (Plating Out)")
with st.form("form_plating_out"):
    col1, col2 = st.columns(2)
    with col1:
        date_out = st.date_input("วันที่ส่งชุบ", datetime.now(), key="date_out")
        qty_out = st.number_input("จำนวนส่งชุบ", min_value=1, value=100, key="qty_out")
        lot_out = st.text_input("Lot No. (ส่งชุบ)", key="lot_out")
        p_no_out = st.text_input("P/No (ส่งชุบ)", key="pno_out")
    with col2:
        p_name_out = st.text_input("PName (ส่งชุบ)", key="pname_out")
        operator_out = st.text_input("ผู้ผลิต", key="op_out")
        plating_type = st.selectbox("ชนิดการชุบ", ["TEP or BC", "TPI or APK", "TI ADT"], key="plating_type")
        log_no = st.text_input("Log. No.", key="log_no")
    
    submitted_out = st.form_submit_button("💾 บันทึกข้อมูลส่งชุบ")
    if submitted_out:
        st.success(f"บันทึกข้อมูลส่งชุบ (Log: {log_no}) เรียบร้อย!")

st.markdown("---")

# ---------------------------------------------------------
# 3. กระบวนการ Stock ชุบ & รับชุบ
# ---------------------------------------------------------
st.header("📦 3. กระบวนการ Stock ชุบ & รับชุบ (Plating In)")
with st.form("form_plating_in"):
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("ส่วน Stock ชุบ")
        stock_remain = st.text_input("เหลือเท่าไร", key="stock_remain")
        stock_where = st.text_input("ที่ไหน", key="stock_where")
    with col2:
        st.subheader("ส่วนรับชุบ")
        date_in = st.date_input("วันที่รับชุบ", datetime.now(), key="date_in")
        qty_in = st.number_input("จำนวนรับ", min_value=1, value=100, key="qty_in")
        lot_in = st.text_input("Lot No. (รับชุบ)", key="lot_in")
        p_no_in = st.text_input("P/No (รับชุบ)", key="pno_in")
        operator_in = st.text_input("ผู้ผลิต (รับชุบ)", key="op_in")
        log_no_in = st.text_input("Log. No. (รับชุบ)", key="log_in_val")
        
    submitted_in = st.form_submit_button("💾 บันทึกข้อมูล Stock/รับชุบ")
    if submitted_in:
        st.success("บันทึกข้อมูลรับชุบเรียบร้อย!")

st.markdown("---")

# ---------------------------------------------------------
# 4. กระบวนการ Stock Component
# ---------------------------------------------------------
st.header("🗄️ 4. Stock Component")
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

st.markdown("---")

# ---------------------------------------------------------
# 5. กระบวนการ Ass'y (Assembly)
# ---------------------------------------------------------
st.header("🛠️ 5. Assembly (Ass'y)")
st.info("โครงสร้างการประกอบ LV1: 17620-Z1T-8010 Cap Comp Fuel Filler")

with st.form("form_assy"):
    col1, col2 = st.columns(2)
    with col1:
        operator_assy = st.text_input("ชื่อพนักงานผู้ประกอบ", key="op_assy")
        lot_assy = st.text_input("Lot ผลิตชิ้นงานสำเร็จรูป", key="lot_assy")
    with col2:
        qty_assy = st.number_input("จำนวนที่ประกอบได้ (Sets)", min_value=1, value=50, key="qty_assy")
    
    st.markdown("**ตรวจสอบรายการชิ้นส่วนประกอบ (LV2):**")
    chk1 = st.checkbox("J0701-17620-Z1T-8000-20 (CAP, OUTER) - ใช้ 1")
    chk2 = st.checkbox("J0701-17620-Z1T-8000-21 (CAP, INNER) - ใช้ 1")
    chk3 = st.checkbox("J0701-17620-Z1T-8000-23 (SPRING, PLATE) - ใช้ 1")
    chk4 = st.checkbox("J0701-17620-Z1T-8000-25 (SEPARATOR, FUEL SUP) - ใช้ 1")
    chk5 = st.checkbox("J0701-17620-Z1T-8000-22 (SEPARATOR, FUEL Sup.B) - ใช้ 1")
    chk6 = st.checkbox("J0701-17631-Z1T-8002 (PACKING, FUEL FILLER) - ใช้ 1")
    chk7 = st.checkbox("J0701-17620-Z1T-8000-24 (RIVET 3x4) - ใช้ 2")
    
    submitted_assy = st.form_submit_button("💾 ยืนยันการประกอบและบันทึกข้อมูล")
    if submitted_assy:
        if chk1 and chk2 and chk3 and chk4 and chk5 and chk6 and chk7:
            st.success(f"ประกอบชิ้นงานสำเร็จ! บันทึก Lot: {lot_assy} เรียบร้อย")
        else:
            st.error("กรุณาตรวจสอบชิ้นส่วนส่วนประกอบ (LV2) ให้ครบทุกรายการก่อนบันทึก")

st.markdown("---")

# ---------------------------------------------------------
# 6. กระบวนการ Stock Cap Comp & Delivery
# ---------------------------------------------------------
st.header("🏁 6. Stock Cap Comp & Delivery")
with st.form("form_delivery"):
    col1, col2 = st.columns(2)
    with col1:
        date_del = st.date_input("วันที่จัดส่ง", datetime.now(), key="date_del")
        product_no = st.text_input("Product No.", value="17620-Z1T-8010 Cap Comp Fuel Filler", key="prod_no")
        delivery_qty = st.number_input("จำนวนจัดส่ง", min_value=1, value=100, key="qty_del")
    with col2:
        destination = st.text_input("ลูกค้า / ปลายทางจัดส่ง", key="dest")
        driver_name = st.text_input("ผู้ส่งมอบ / เจ้าหน้าที่", key="driver")
        
    submitted_del = st.form_submit_button("💾 บันทึกข้อมูลจัดส่ง")
    if submitted_del:
        st.success(f"บันทึกข้อมูลจัดส่งสินค้าจำนวน {delivery_qty} ชิ้น เรียบร้อย!")
