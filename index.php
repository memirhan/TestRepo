<?php
// Kullanıcıdan veri al
$input = $_GET['q'];

// Çıktıyı HTML özel karakterlerden kaçırarak ekrana bas
echo "Arama sonucu: " . htmlspecialchars($input, ENT_QUOTES, 'UTF-8');
?>