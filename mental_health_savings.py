import streamlit as st

def calculate_savings(investment, avg_salary, employees, productivity_boost, turnover_reduction, sick_leave_reduction):
    """
    Рассчитывает экономию компании при вложении в ментальное здоровье сотрудников.
    """
    annual_salary = avg_salary * 12
    
    # Предполагаемая экономия
    productivity_gain = (productivity_boost / 100) * annual_salary * employees
    turnover_savings = (turnover_reduction / 100) * annual_salary * employees * 0.5  # 50% годового оклада на замену
    sick_leave_savings = (sick_leave_reduction / 100) * annual_salary * employees
    
    total_savings = productivity_gain + turnover_savings + sick_leave_savings - investment
    return total_savings

# Интерфейс Streamlit
st.title("Калькулятор экономии на инвестициях в ментальное здоровье сотрудников")

# Входные данные
investment = st.number_input("Сумма инвестиций в ментальное здоровье ($):", min_value=0.0, value=10000.0, step=1000.0)
employees = st.number_input("Количество сотрудников:", min_value=1, value=100)
productivity_boost = st.slider("Ожидаемый рост продуктивности (%):", 0, 20, 5)
turnover_reduction = st.slider("Ожидаемое снижение текучести кадров (%):", 0, 20, 5)
sick_leave_reduction = st.slider("Ожидаемое сокращение больничных дней (%):", 0, 20, 5)

# Фиксированное значение средней зарплаты
avg_salary = 1500.0

# Расчет
savings = calculate_savings(investment, avg_salary, employees, productivity_boost, turnover_reduction, sick_leave_reduction)

# Вывод результата
st.write(f"### Ожидаемая экономия: ${savings:,.2f}")
