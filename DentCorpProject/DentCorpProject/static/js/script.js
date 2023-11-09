document.addEventListener("DOMContentLoaded", function () {
    const calendarTable = document.getElementById("calendarTable");
    const calendarBody = document.getElementById("calendarBody");
    const monthYearDisplay = document.getElementById("monthYearDisplay");
    const prevMonthBtn = document.getElementById("prevMonth");
    const nextMonthBtn = document.getElementById("nextMonth");

    let currentDate = new Date();

    function updateCalendar() {
        while (calendarBody.firstChild) {
            calendarBody.removeChild(calendarBody.firstChild);
        }

        const firstDay = new Date(currentDate.getFullYear(), currentDate.getMonth(), 1);
        const lastDay = new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 0);
        const startingDay = firstDay.getDay();
        const daysInMonth = lastDay.getDate();

        monthYearDisplay.textContent = `${new Intl.DateTimeFormat('es-ES', { month: 'long', year: 'numeric' }).format(currentDate)}`;

        let day = 1;
        for (let i = 0; i < 6; i++) {
            const row = document.createElement("tr");
            for (let j = 0; j < 7; j++) {
                const cell = document.createElement("td");
                if (i === 0 && j < startingDay) {
                    // Celdas vacías antes del primer día del mes
                } else if (day > daysInMonth) {
                    // Celdas vacías después del último día del mes
                } else {
                    cell.textContent = day;
                    if (currentDate.getFullYear() === new Date().getFullYear() && currentDate.getMonth() === new Date().getMonth() && day === new Date().getDate()) {
                        cell.classList.add("today");
                    }
                    day++;
                }
                row.appendChild(cell);
            }
            calendarBody.appendChild(row);
        }
    }

    prevMonthBtn.addEventListener("click", () => {
        currentDate.setMonth(currentDate.getMonth() - 1);
        updateCalendar();
    });

    nextMonthBtn.addEventListener("click", () => {
        currentDate.setMonth(currentDate.getMonth() + 1);
        updateCalendar();
    });

    updateCalendar();
});
