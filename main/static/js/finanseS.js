document.addEventListener("DOMContentLoaded", () => {
    const modalOverlay = document.getElementById("modal-overlay");
    const openModalBtn = document.querySelector(".open-modal-btn");
    const closeModalBtn = document.getElementById("close-modal-btn");
    const modalOverlay1 = document.getElementById("modal-overlay1");
    const openModalBtn1 = document.querySelector(".open-modal-btn1");
    const closeModalBtn1 = document.getElementById("close-modal-btn1");
    const modalOverlay2 = document.getElementById("modal-overlay2");
    const openModalBtn2 = document.querySelector(".open-modal-btn2");
    const closeModalBtn2 = document.getElementById("close-modal-btn2");

    if (openModalBtn) {
        openModalBtn.addEventListener("click", () => {
            modalOverlay.style.display = "block";
        });
    }

    if (closeModalBtn) {
        closeModalBtn.addEventListener("click", () => {
            modalOverlay.style.display = "none";
        });
    }




    if (openModalBtn1) {
        openModalBtn1.addEventListener("click", () => {
            modalOverlay1.style.display = "block";
        });
    }

    if (closeModalBtn1) {
        closeModalBtn1.addEventListener("click", () => {
            modalOverlay1.style.display = "none";
        });
    }



    if (openModalBtn2) {
        openModalBtn2.addEventListener("click", () => {
            modalOverlay2.style.display = "block";
        });
    }

    if (closeModalBtn2) {
        closeModalBtn2.addEventListener("click", () => {
            modalOverlay2.style.display = "none";
        });
    }
});