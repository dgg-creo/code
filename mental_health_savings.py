import streamlit as st

def calculate_savings(avg_salary, employees, investment):
    """
    Розраховує економію компанії при інвестуванні в ментальне здоров'я співробітників.
    """
    annual_salary = avg_salary * 12
    
    # Автоматичний розрахунок впливу інвестицій (приблизні коефіцієнти)
    productivity_boost = min(0.0005 * investment, 20)  # Не більше 20%
    turnover_reduction = min(0.0003 * investment, 15)  # Не більше 15%
    sick_leave_reduction = min(0.0002 * investment, 10)  # Не більше 10%
    
    # Розрахунок окремих складових економії
    productivity_gain = (productivity_boost / 100) * annual_salary * employees
    turnover_savings = (turnover_reduction / 100) * annual_salary * employees * 0.5  # 50% річного окладу на заміну
    sick_leave_savings = (sick_leave_reduction / 100) * annual_salary * employees
    
    total_savings = productivity_gain + turnover_savings + sick_leave_savings - investment
    savings_per_employee = total_savings / employees if employees > 0 else 0
    
    return productivity_boost, turnover_reduction, sick_leave_reduction, productivity_gain, turnover_savings, sick_leave_savings, total_savings, savings_per_employee

# Інтерфейс Streamlit
st.title("Калькулятор економії на інвестиціях у ментальне здоров'я співробітників")

# Вхідні дані
avg_salary = st.number_input("Середня заробітна плата ($):", min_value=0.0, value=1500.0, step=100.0)
employees = st.number_input("Кількість співробітників:", min_value=1, value=100)
investment = st.number_input("Сума вкладень у ментальне та психологічне здоров'я ($) на рік:", min_value=0.0, value=10000.0, step=1000.0)

# Розрахунок
productivity_boost, turnover_reduction, sick_leave_reduction, productivity_gain, turnover_savings, sick_leave_savings, total_savings, savings_per_employee = calculate_savings(avg_salary, employees, investment)

# Вивід результатів
st.subheader("Результати економії:")
st.write(f"🔹 Очікуване зростання продуктивності: {productivity_boost:.2f}%")
st.write(f"🔹 Очікуване зниження плинності кадрів: {turnover_reduction:.2f}%")
st.write(f"🔹 Очікуване скорочення лікарняних: {sick_leave_reduction:.2f}%")

st.subheader("Економія для компанії:")
st.write(f"🔹 Збільшення продуктивності: ${productivity_gain:,.2f}")
st.write(f"🔹 Економія за рахунок зменшення плинності кадрів: ${turnover_savings:,.2f}")
st.write(f"🔹 Економія за рахунок скорочення лікарняних: ${sick_leave_savings:,.2f}")
st.write(f"### Загальна економія за рік: ${total_savings:,.2f}")

st.subheader("Економія на одного співробітника:")
st.write(f"### ${savings_per_employee:,.2f} на рік")
