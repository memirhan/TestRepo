<!DOCTYPE html>
<html>
<head>
    <title>XSS Demo</title>
</head>
<body>

    <h2>Yorum Sistemi</h2>

    <input type="text" id="comment" placeholder="Yorum yaz">
    <button onclick="addComment()">Gönder</button>

    <div id="comments"></div>

    <script>
        function addComment() {
            const input = document.getElementById("comment").value;

            const commentsDiv = document.getElementById("comments");
            const pElement = document.createElement("p");
            pElement.textContent = input; // Güvenli: Kullanıcı girdisi güvenli bir şekilde metin olarak ekleniyor.
            commentsDiv.appendChild(pElement);
        }
    </script>

</body>
</html>