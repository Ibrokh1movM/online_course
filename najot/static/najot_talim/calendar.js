document.addEventListener("DOMContentLoaded", function () {
    flatpickr("#calendar", {
        dateFormat: "Y-m-d",
        defaultDate: new Date(),
        inline: true,
        disable: [
            function (date) {
                return ![2, 4, 6].includes(date.getDay());
            }
        ],
        onDayCreate: function (dObj, dStr, fp, dayElem) {
            let date = new Date(dayElem.dateObj);
            let today = new Date();
            today.setHours(0, 0, 0, 0);

            if ([2, 4, 6].includes(date.getDay())) {
                if (date < today) {
                    dayElem.classList.add("past-dars");
                } else {
                    dayElem.classList.add("future-dars");
                }
            }
            if (!dayElem.classList.contains("prevMonthDay") && !dayElem.classList.contains("nextMonthDay")) {
                return;
            }
            dayElem.classList.add("otherMonth");
        },
        onChange: function (selectedDates, dateStr) {
            let selectedDate = new Date(dateStr);
            let today = new Date();
            today.setHours(0, 0, 0, 0); // Faqat sana qismi solishtiriladi

            if (selectedDate >= today) {
                let confirmLesson = confirm("Darsni boshlaysizmi?");
                if (!confirmLesson) {
                    return; // Agar foydalanuvchi rad etsa, hech narsa qilinmaydi
                }
            }

            // Faqat tasdiqlangandan keyin yoki o'tmishdagi kunlar avtomatik ravishda yuboriladi
            window.location.href = `/students/?date=${dateStr}`;
        }
    });
});
