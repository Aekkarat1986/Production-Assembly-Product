import streamlit as st
import pandas as pd
from datetime import datetime

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="Jozu Auto Part - Production Control", page_icon="🏭", layout="wide")

st.title("🏭 Jozu Auto Part: Production & Assembly Control System")
st.markdown("---")

# เมนูด้านข้างสำหรับเลือกโหมดการทำงาน
menu = st.sidebar.selectbox("เลือกเมนูระบบ", [
    "1. บันทึกข้อมูลการผลิต (Web Form)", 
    "2. ตรวจสอบชิ้นส่วนด้วย Barcode (Anti-Error)", 
    "3. แดชบอร์ดการผลิต (Dashboard)"
])

# ---------------------------------------------------------
# เมนูที่ 1: ระบบฟอร์มบันทึกข้อมูลการผลิต
# ---------------------------------------------------------
if menu == "1. บันทึกข้อมูลการผลิต (Web Form)":
    st.header("📝 ฟอร์มบันทึกข้อมูลการผลิต (Production Record)")
    
    with st.form("prod_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            prod_date = st.date_input("วันที่ผลิต", datetime.now())
            process_step = st.selectbox("กระบวนการผลิต", ["Press", "Stock ชุบ", "Stock Component", "Assembly (Ass'y)", "Delivery"])
            lot_no = st.text_input("Lot No. (เช่น LOT-2026-0301)")
            
        with col2:
            operator_name = st.text_input("ชื่อพนักงานผู้บันทึก/ผู้ผลิต")
            part_no = st.selectbox("Part Number หลัก", [
                "17620-Z1T-8010 (Cap Comp Fuel Filler)",
                "J0701-17620-Z1T-8000-20 (CAP, OUTER)",
                "J0701-17620-Z1T-8000-21 (CAP, INNER)"
            ])
            quantity = st.number_input("จำนวนชิ้นงาน (Qty)", min_value=1, value=100)
            
        qc_status = st.radio("ผลการตรวจสอบคุณภาพ (QC Status)", ["Pass (ผ่าน)", "Fail (ไม่ผ่าน - กักกัน)"])
        note = st.text_area("หมายเหตุเพิ่มเติม (ถ้ามี)")
        
        submitted = st.form_submit_button("💾 บันทึกข้อมูลเข้าสู่ระบบ")
        
        if submitted:
            if lot_no and operator_name:
                st.success(f"บันทึกข้อมูลกระบวนการ [{process_step}] ของ Lot: {lot_no} สำเร็จเรียบร้อย!")
                # (สามารถเขียนโค้ดบันทึกลง Database หรือ Google Sheets เพิ่มเติมตรงนี้ได้)
            else:
                st.error("กรุณากรอกข้อมูล Lot No. และชื่อพนักงานให้ครบถ้วน")

# ---------------------------------------------------------
# เมนูที่ 2: ระบบตรวจสอบชิ้นส่วน (Barcode / QR Scanner Anti-Error)
# ---------------------------------------------------------
elif menu == "2. ตรวจสอบชิ้นส่วนด้วย Barcode (Anti-Error)":
    st.header("🔍 ระบบสแกนตรวจสอบชิ้นส่วนก่อนประกอบ (Poka-Yoke / Anti-Error)")
    st.info("ใช้สำหรับสแกนหรือพิมพ์รหัส Part เพื่อตรวจสอบความถูกต้องของชิ้นส่วนประกอบชุด LV2 ก่อนเข้าไลน์ Assembly")

    scanned_part = st.text_input("สแกนหรือพิมพ์ Part Number ชิ้นส่วน:")
    
    # กำหนดฐานข้อมูลสเปกที่ถูกต้องสำหรับประกอบ Cap Comp (17620-Z1T-8010)
    valid_parts = {
        "J0701-17620-Z1T-8000-20": "CAP, OUTER (จำนวนที่ใช้: 1)",
        "J0701-17620-Z1T-8000-21": "CAP, INNER (จำนวนที่ใช้: 1)",
        "J0701-17620-Z1T-8000-23": "SPRING, PLATE (จำนวนที่ใช้: 1)",
        "J0701-17620-Z1T-8000-25": "SEPARATOR, FUEL SUP (จำนวนที่ใช้: 1)",
        "J0701-17620-Z1T-8000-22": "SEPARATOR, FUEL (Sup.B) (จำนวนที่ใช้: 1)",
        "J0701-17631-Z1T-8002": "PACKING, FUEL FILLER (จำนวนที่ใช้: 1)",
        "J0701-17620-Z1T-8000-24": "RIVET 3x4 (จำนวนที่ใช้: 2)"
    }
    
    if scanned_part:
        if scanned_part in valid_parts:
            st.success(f"✅ ถูกต้อง! ชิ้นส่วนนี้ใช้สำหรับประกอบ Cap Comp: {valid_parts[scanned_part]}")
        else:
            st.error("❌ แจ้งเตือน! พาร์ทนี้ไม่ถูกต้องหรือไม่อยู่ในรายการประกอบของรุ่นนี้ ห้ามนำเข้าไลน์ผลิต!")

# ---------------------------------------------------------
# เมนูที่ 3: แดชบอร์ดแสดงผล (Production Dashboard)
# ---------------------------------------------------------
elif menu == "3. แดชบอร์ดการผลิต (Dashboard)":
    st.header("📊 แดชบอร์ดสรุปผลการผลิต (Real-time Production Status)")
    
    # จำลองข้อมูลตัวเลขสรุป
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("เป้าหมายการผลิตวันนี้", "1,200 ชิ้น")
    col2.metric("ผลิตได้จริง (Actual)", "950 ชิ้น", "+12%")
    col3.metric("ของเสีย (Defect)", "4 ชิ้น", "-2 ชิ้น")
    col4.metric("สถานะไลน์ผลิต", "🟢 ปกติ (Running)")
    
    st.markdown("---")
    st.subheader("📋 ประวัติการผลิตล่าสุดประจำวัน")
    
    # จำลองตารางข้อมูลตัวอย่าง
    chart_data = pd.DataFrame({
        "เวลา": ["08:00", "10:00", "12:00", "14:00"],
        "กระบวนการ": ["Press", "Stock ชุบ", "Assembly", "Delivery"],
        "Lot No.": ["LOT-2603-01", "LOT-2603-02", "LOT-2603-03", "LOT-2603-04"],
        "จำนวน (pcs)": [300, 280, 250, 120],
        "สถานะ QC": ["Pass", "Pass", "Pass", "Pass"]
    })
    
    st.dataframe(chart_data, use_container_width=True)
