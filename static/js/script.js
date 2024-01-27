function setProposalHeading(username) {
  document.getElementById("proposalHeading").innerText =
    username + ", do you want to go out with me?";
}

function promptName() {
  let username = "";

  while (username == null || username == "") {
    username = prompt("Please enter your name:");
  }

  document.getElementById("username").value = username;
  setProposalHeading(username);
}

formContent = document.getElementById("proposalForm");
if (formContent != null) {
  promptName();
}
