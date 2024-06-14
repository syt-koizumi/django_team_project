const questions = [
    {
        question: "あなたにおすすめの映画を探します。",
        choices: ["スタートする"],
        answer: "スタートする"
    },
    {
        question: "ホラー映画は見たい?",
        choices: ["はい", "いいえ"],
        answer: "はい"
    },
    {
        question: "アクション映画は見たい?",
        choices: ["はい", "いいえ"],
        answer: "はい"
    },
    {
        question: "アニメ映画は見たい?",
        choices: ["はい", "いいえ"],
        answer: "はい"
    },
    {
        question: "恋愛映画は見たい?",
        choices: ["はい", "いいえ"],
        answer: "はい"
    },
    {
        question: "ミステリー映画は見たい?",
        choices: ["はい", "いいえ"],
        answer: "はい"
    },
    {
        question: "アドベンチャー映画は見たい?",
        choices: ["はい", "いいえ"],
        answer: "はい"
    },
    {
        question: "コメディ映画は見たい?",
        choices: ["はい", "いいえ"],
        answer: "はい"
    },
    {
        question: "SF映画は見たい?",
        choices: ["はい", "いいえ"],
        answer: "はい"
    },
    // Add more questions here
];

let currentQuestion = 0;
let score = [];

function displayQuestion() {
    const questionElement = document.getElementById("question");
    const choicesElement = document.getElementById("choices");

    questionElement.textContent = questions[currentQuestion].question;
    choicesElement.innerHTML = "";

    questions[currentQuestion].choices.forEach(choice => {
        const button = document.createElement("button");
        button.textContent = choice;
        button.onclick = function() {
            check(choice);
        };
        choicesElement.appendChild(button);
    });
}

function check(choice) {
    if(choice=="スタートする"){
        score.push(scoretaiou);
    }
    else if (choice === questions[currentQuestion].answer) {
        score.push("True");
    }
    else{
        score.push("False");
    }
    currentQuestion++;
    if (currentQuestion < questions.length) {
        displayQuestion();
    } else {
        showResult();
    }
}

function showResult() {
    const quizContainer = document.getElementById("quiz-container");
    console.log(score);
    quizContainer.innerHTML = `<h2>Quiz Completed</h2><p>Your score: ${score}</p>`;
}

displayQuestion();