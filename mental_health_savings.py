import streamlit as st

def calculate_savings(avg_salary, employees, investment):
    """
    Рассчитывает экономию компании при вложении в ментальное здоровье сотрудников.
    """
    annual_salary = avg_salary * 12
    
    # Автоматический расчет влияния инвестиций (примерные коэффициенты)
    productivity_boost = min(0.0005 * investment, 20)  # Не более 20%
    turnover_reduction = min(0.0003 * investment, 15)  # Не более 15%
    sick_leave_reduction = min(0.0002 * investment, 10)  # Не более 10%
    
    # Рассчитываем отдельные составляющие экономии
    productivity_gain = (productivity_boost / 100) * annual_salary * employees
    turnover_savings = (turnover_reduction / 100) * annual_salary * employees * 0.5  # 50% от годового оклада на замену
    sick_leave_savings = (sick_leave_reduction / 100) * annual_salary * employees
    
    total_savings = productivity_gain + turnover_savings + sick_leave_savings - investment
    savings_per_employee = total_savings / employees if employees > 0 else 0
    
    return productivity_boost, turnover_reduction, sick_leave_reduction, productivity_gain, turnover_savings, sick_leave_savings, total_savings, savings_per_employee

# Интерфейс Streamlit
st.title("Калькулятор экономии на инвестициях в ментальное здоровье сотрудников")

# Входные данные
avg_salary = st.number_input("Средняя заработная плата ($):", min_value=0.0, value=1500.0, step=100.0)
employees = st.number_input("Количество сотрудников:", min_value=1, value=100)
investment = st.number_input("Сумма вклада в ментальное и психическое здоровье ($):", min_value=0.0, value=10000.0, step=1000.0)

# Расчет
productivity_boost, turnover_reduction, sick_leave_reduction, productivity_gain, turnover_savings, sick_leave_savings, total_savings, savings_per_employee = calculate_savings(avg_salary, employees, investment)

# Вывод результатов
st.subheader("Результаты экономии:")
st.write(f"🔹 Ожидаемый рост продуктивности: {productivity_boost:.2f}%")
st.write(f"🔹 Ожидаемое снижение текучести: {turnover_reduction:.2f}%")
st.write(f"🔹 Ожидаемое сокращение больничных: {sick_leave_reduction:.2f}%")

st.subheader("Экономия для компании:")
st.write(f"🔹 Рост продуктивности: ${productivity_gain:,.2f}")
st.write(f"🔹 Экономия за счет снижения текучести: ${turnover_savings:,.2f}")
st.write(f"🔹 Экономия за счет сокращения больничных: ${sick_leave_savings:,.2f}")
st.write(f"### Общая экономия за год: ${total_savings:,.2f}")

st.subheader("Экономия на одного сотрудника:")
st.write(f"### ${savings_per_employee:,.2f} в год")
