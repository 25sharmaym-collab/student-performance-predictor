const form = document.querySelector("#prediction-form");
const result = document.querySelector("#result");

const fields = [
  ["study_hours", "study-output", v => Number(v).toFixed(1)],
  ["attendance", "attendance-output", v => v + "%"],
  ["previous_marks", "previous-output", v => v + "%"],
  ["assignments_completed", "assignments-output", v => v + "/10"],
  ["internal_marks", "internal-output", v => v + "%"],
  ["sleep_hours", "sleep-output", v => Number(v).toFixed(1)]
];

fields.forEach(([name, outputId, format]) => {
  const input = form.elements[name];
  const output = document.getElementById(outputId);
  const update = () => output.textContent = format(input.value);
  input.addEventListener("input", update);
  update();
});

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  form.classList.add("loading");

  const payload = Object.fromEntries(new FormData(form).entries());
  payload.study_hours = Number(payload.study_hours);
  payload.attendance = Number(payload.attendance);
  payload.previous_marks = Number(payload.previous_marks);
  payload.assignments_completed = Number(payload.assignments_completed);
  payload.internal_marks = Number(payload.internal_marks);
  payload.sleep_hours = Number(payload.sleep_hours);

  try {
    const response = await fetch("/api/predict", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(payload)
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.detail?.[0]?.msg || "Prediction failed.");

    result.classList.remove("empty");
    result.innerHTML = `
      <p class="eyebrow">YOUR RESULT</p>
      <h2>Performance snapshot</h2>
      <div class="score-row">
        <span class="score">${data.predicted_score}</span>
        <span class="score-unit">/ 100</span>
      </div>
      <div class="badges">
        <span class="badge">${data.performance} performance</span>
        <span class="badge">${data.risk} risk</span>
      </div>
      <div class="result-block">
        <h3>What to focus on</h3>
        <ul>${data.advice.map(item => `<li>${item}</li>`).join("")}</ul>
      </div>
      <div class="result-block">
        <h3>Important</h3>
        <p style="color:#75808a;line-height:1.55;font-size:13px;margin:0">
          This is a model-based estimate from the project's training data. Use it as a learning tool, not as an official academic result.
        </p>
      </div>
    `;
    result.scrollIntoView({behavior: "smooth", block: "nearest"});
  } catch (error) {
    result.innerHTML = `<div class="error">${error.message}</div>`;
  } finally {
    form.classList.remove("loading");
  }
});
