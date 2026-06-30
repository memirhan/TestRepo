<?php
// DİKKAT: Bu kod kasıtlı olarak XSS'e açıktır.

$name = $_GET['name'] ?? '';

echo "<h1>Merhaba $name</h1>";
