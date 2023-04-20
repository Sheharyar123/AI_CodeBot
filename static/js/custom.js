document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("#main-form");
  const loader = document.querySelector("#loader");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      loader.style.display = "block";
      const code = document.querySelector("#code").value;
      const lang = document.querySelector("#lang").value;
      const csrf_token = document.querySelector(
        "input[name=csrfmiddlewaretoken"
      ).value;

      $.ajax({
        type: "POST",
        url: "/",
        data: { code: code, lang: lang, csrfmiddlewaretoken: csrf_token },
        success: function (response) {
          if (response.status === "success") {
            const newCode = document.querySelector("#new_code");
            newCode.classList.remove("language-python");
            newCode.classList.add(`language-${lang.toLowerCase()}`);
            newCode.innerHTML = response.code;
            Prism.highlightAll();
          } else {
            swal({
              title: "You forgot to select the programming language",
              text: "",
              icon: "error",
            });
          }
          form.reset();
          loader.style.display = "none";
        },
      });
    });
  }

  const suggestForm = document.querySelector("#suggest_form");
  if (suggestForm) {
    suggestForm.addEventListener("submit", function (e) {
      e.preventDefault();
      loader.style.display = "block";
      const code = document.querySelector("#suggest_code").value;
      const lang = document.querySelector("#suggest_lang").value;
      const url = document.querySelector("#url").value;
      console.log(url);
      const csrf_token = document.querySelector(
        "input[name=csrfmiddlewaretoken"
      ).value;
      console.log(lang);

      $.ajax({
        type: "POST",
        url: url,
        data: { code: code, lang: lang, csrfmiddlewaretoken: csrf_token },
        success: function (response) {
          if (response.status === "success") {
            const newCode = document.querySelector("#new_code");
            newCode.classList.remove("language-python");
            newCode.classList.add(`language-${lang.toLowerCase()}`);
            newCode.innerHTML = response.code;
            Prism.highlightAll();
          } else {
            swal({
              title: "You forgot to select the programming language",
              text: "",
              icon: "error",
            });
          }
          suggestForm.reset();
          loader.style.display = "none";
        },
      });
    });
  }
});
