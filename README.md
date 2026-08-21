<div align="center">

# 🏭 PRODUCTION FLOW & PROCESS MANUAL
## CAP COMP FUEL FILLER (17620-Z1T-8010)

<br>

<!-- ปุ่มกดขนาดใหญ่พิเศษ -->
<a href="https://jozu-factory-app.streamlit.app" target="_blank">
    <img src="https://img.shields.io/badge/🚀_เปิดระบบบันทึกข้อมูลการผลิต_(STREAMLIT_APP)-brightgreen?style=for-the-badge&logo=streamlit&labelColor=111111" alt="Open App" width="550">
</a>

<br><br>
<p style="font-size: 16px; font-weight: bold; color: #555;">📌 คลิกปุ่มด้านบนเพื่อเข้าสู่ระบบฟอร์มบันทึกข้อมูลการปฏิบัติงานประจำวัน</p>

</div>

<hr>

## 🔄 ผังกระบวนการผลิต (Process Flow Diagram)

```mermaid
graph TD
    A["1. Press Process <br> 🛠️ ปั๊มขึ้นรูปชิ้นส่วนโลหะและพลาสติก"] --> B["2. Plating / Stock ชุบ <br> 🧪 ชุบผิวชิ้นงานและบันทึก Lot"]
    B --> C["3. Stock Component <br> 📦 จัดเก็บและควบคุมสต็อกชิ้นส่วน"]
    C --> D["4. Assembly Ass'y <br> ⚙️ ประกอบชิ้นส่วนตามมาตรฐาน"]
    D --> E["5. Stock & Delivery <br> 🚚 ตรวจสอบสำเร็จรูปและจัดส่ง"]

    style A fill:#e3f2fd,stroke:#1565c0,stroke-width:2px,color:#000
    style B fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#000
    style C fill:#fff3e0,stroke:#ef6c00,stroke-width:2px,color:#000
    style D fill:#fce4ec,stroke:#c2185b,stroke-width:2px,color:#000
    style E fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#000
