import streamlit as st

st.set_page_config(page_title="نظام التنبؤ المبكر بالتعثر الدراسي", layout="centered")

st.title("🎓 نظام التنبؤ المبكر بالتعثر الدراسي")
st.write("واجهة تحليل ومتابعة حالة الطالب لوزارة التربية والتعليم")

st.subheader("إدخال بيانات الطالب")

absences = st.slider("عدد أيام الغياب", 0, 30, 5)
previous_grade = st.slider("علامة الفصل السابق", 30, 100, 75)
study_hours = st.slider("ساعات الدراسة الأسبوعية", 1, 40, 15)

if st.button("تحليل حالة الطالب"):
    # شرط محاكاة للتنبؤ
    if absences > 10 or previous_grade < 50:
        st.error("⚠️ الطالب معرض للتعثر الدراسي! يتطلب التدخل المبكر.")
    else:
        st.success("✅ حالة الطالب مستقرة وطبيعية.")
