import streamlit as st

def calculate_savings(avg_salary, employees, investment, productivity_boost, turnover_reduction, sick_leave_reduction):
    """
    Рассчитывает экономию компании при вложении в ментальное здоровье сотрудников.
    """
    annual_salary = avg_salary * 12
    
    # Рассчитываем отдельные составляющие экономии
    productivity_gain = (productivity_boost / 100) * annual_salary * employees
    turnover_savings = (turnover_reduction / 100) * annual_salary * employees * 0.5  # 50% от годового оклада на замену
    sick_leave_savings = (sick_leave_reduction / 100) * annual_salary * employees
    
    total_savings = productivity_gain + turnover_savings + sick_leave_savings - investment
    return productivity_gain, turnover_savings, sick_leave_savings, total_savings

# Интерфейс Streamlit
st.title("Калькулятор экономии на инвестициях в ментальное здоровье сотрудников")

# Входные данные
avg_salary = st.number_input("Средняя заработная плата ($):", min_value=0.0, value=1500.0, step=100.0)
employees = st.number_input("Количество сотрудников:", min_value=1, value=100)
investment = st.number_input("Сумма вклада в ментальное и психическое здоровье ($):", min_value=0.0, value=10000.0, step=1000.0)
productivity_boost = st.slider("Ожидаемый рост продуктивности (%):", 0, 20, 5)
turnover_reduction = st.slider("Ожидаемое снижение текучести кадров (%):", 0, 20, 5)
sick_leave_reduction = st.slider("Ожидаемое сокращение больничных дней (%):", 0, 20, 5)

# Расчет
productivity_gain, turnover_savings, sick_leave_savings, total_savings = calculate_savings(avg_salary, employees, investment, productivity_boost, turnover_reduction, sick_leave_reduction)

# Вывод результатов
st.subheader("Результаты экономии:")
st.write(f"🔹 Рост продуктивности: ${productivity_gain:,.2f}")
st.write(f"🔹 Экономия за счет снижения текучести: ${turnover_savings:,.2f}")
st.write(f"🔹 Экономия за счет сокращения больничных: ${sick_leave_savings:,.2f}")
st.write(f"### Общая экономия: ${total_savings:,.2f}")
