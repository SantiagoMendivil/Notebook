let homeScore = document.getElementById("home-score").querySelector("h2");
let visitorScore = document.getElementById("visitor-score").querySelector("h2");
let homePanel = document.getElementById("home");
let visitorPanel = document.getElementById("visitor");
let resetButton = document.getElementById("reset-button");

document.getElementById("home-3points").addEventListener("click", function () {
    updateScore(homeScore, 3);
});
document.getElementById("home-2points").addEventListener("click", function () {
    updateScore(homeScore, 2);
});
document.getElementById("home-1point").addEventListener("click", function () {
    updateScore(homeScore, 1);
});

document.getElementById("visitor-3points").addEventListener("click", function () {
    updateScore(visitorScore, 3);
});
document.getElementById("visitor-2points").addEventListener("click", function () {
    updateScore(visitorScore, 2);
});
document.getElementById("visitor-1point").addEventListener("click", function () {
    updateScore(visitorScore, 1);
});

resetButton.addEventListener("click", resetScore);

function updateScore(element, points) {
    let currentScore = parseInt(element.textContent);
    element.textContent = currentScore + points;
    checkScores();
}

function resetScore() {
    homeScore.textContent = 0;
    visitorScore.textContent = 0;
    checkScores();
}

function checkScores() {
    let homeScoreValue = parseInt(homeScore.textContent);
    let visitorScoreValue = parseInt(visitorScore.textContent);

    if (homeScoreValue > visitorScoreValue) {
        homePanel.style.backgroundColor = "green";
        visitorPanel.style.backgroundColor = "red";
    } else if (homeScoreValue < visitorScoreValue) {
        homePanel.style.backgroundColor = "red";
        visitorPanel.style.backgroundColor = "green";
    } else {
        homePanel.style.backgroundColor = "white";
        visitorPanel.style.backgroundColor = "white";
    }
}

checkScores();