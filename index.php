<!DOCTYPE html>
<html>
<head>
    <title>XSS Demodddd</title>
</head>
<body>

    <h2>Yorum Sistemi</h2>

    <input type="text" id="comment" placeholder="Yorum sssyaz">
    <button onclick="addComment()">Gönder</button>

    <div id="comments"></div>

    <script>
        function addComment() {
            const input = document.getElementById("comment").value;

            // ❌ Güvensiz: Kullanıcı girdisi doğrudan HTML olarak ekleniyor.
            document.getElementById("comments").innerHTML +=
                "<p>" + input + "</p>";
        }
    </script>

</body>
</html>
