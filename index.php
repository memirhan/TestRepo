<?php
// Kullanıcıdan veri al
$input = $_GET['q'];

// Direkt ekrana bas (XSS açığı!)
echo "Arama sonucu: " . $input;
?>
