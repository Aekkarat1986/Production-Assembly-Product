<!-- ปุ่มกดลิงก์ไปหน้าบันทึกข้อมูล -->
<div align="center">
    <a href="https://jozu-factory-app.streamlit.app" target="_blank">
        <img src="https://img.shields.io/badge/🚀_เปิดระบบบันทึกข้อมูลการผลิต_(Streamlit_App)-brightgreen?style=for-the-badge&logo=streamlit" alt="Open App" width="100%">
    </a>
</div>

---

# 🏭 Production Flow: Cap Comp

คู่มือผังการไหลของกระบวนการผลิตผลิตภัณฑ์ **Cap Comp Fuel Filler (17620-Z1T-8010)**

---

## 🔄 ผังกระบวนการผลิต (Process Flow Diagram)

```mermaid
graph TD
    A[1. Press Process <br> ปั๊มขึ้นรูปชิ้นส่วน] --> B[2. Plating & Stock <br> ชุบผิวและคุมสต็อกชุบ]
    B --> C[3. Stock Component <br> จัดเก็บชิ้นส่วนย่อย]
    C --> D[4. Assembly Ass'y <br> ประกอบชิ้นส่วน]
    D --> E[5. Stock & Delivery <br> ตรวจสอบและจัดส่ง]
    
    style A fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style B fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style C fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    style D fill:#fce4ec,stroke:#c2185b,stroke-width:2px
    style E fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
