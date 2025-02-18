document.getElementById("scheduleForm").addEventListener("submit", async (event) => {
    event.preventDefault();
    let platform = document.getElementById("platform").value;
    let content = document.getElementById("content").value;
    let scheduled_time = document.getElementById("scheduled_time").value;

    let response = await fetch("http://127.0.0.1:5000/schedule", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ platform, content, scheduled_time })
    });

    let result = await response.json();
    alert(result.message);
});
