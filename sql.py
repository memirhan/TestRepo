<?php
// Veritabanı bağlantısı
$host = "localhost";
$username = "root";
$password = "";
$database = "test_db";

$conn = mysqli_connect($host, $username, $password, $database);

// Kullanıcı girdisini doğrudan sorguya ekleme - ÇOK TEHLİKELİ!
$kullanici_adi = $_POST['username'];
$sifre = $_POST['password'];

// Güvensiz sorgu
$query = "SELECT * FROM kullanicilar WHERE username = '$kullanici_adi' AND password = '$sifre'";

$result = mysqli_query($conn, $query);

if(mysqli_num_rows($result) > 0) {
    echo "Giriş başarılı!";
} else {
    echo "Hatalı kullanıcı adı veya şifre!";
}
?>
