import streamlit as st

def calculate_savings(avg_salary, employees, investment):
    """
    Рассчитывает экономию компании при вложении в ментальное здоровье сотрудников.
    """
    annual_salary = avg_salary * 12
    
    # Оценочные коэффициенты
    productivity_boost = 0.05  # 5% рост продуктивности
    turnover_reduction = 0.05  # 5% снижение текучести
    sick_leave_reduction = 0.05  # 5% снижение больничных
    
    productivity_gain = productivity_boost * annual_salary * employees
    turnover_savings = turnover_reduction * annual_salary * employees * 0.5  # 50% годового оклада на замену
    sick_leave_savings = sick_leave_reduction * annual_salary * employees
    
    total_savings = productivity_gain + turnover_savings + sick_leave_savings - investment
    return total_savings

# Интерфейс Streamlit
st.title("Калькулятор экономии на инвестициях в ментальное здоровье сотрудников")

# Входные данные
avg_salary = st.number_input("Средняя заработная плата ($):", min_value=0.0, value=1500.0, step=100.0)
employees = st.number_input("Количество сотрудников:", min_value=1, value=100)
investment = st.number_input("Сумма вклада в ментальное и психическое здоровье ($):", min_value=0.0, value=10000.0, step=1000.0)

# Расчет
savings = calculate_savings(avg_salary, employees, investment)

# Вывод результата
st.write(f"### Ожидаемая экономия: ${savings:,.2f}")
