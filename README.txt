Opis zadania
Celem zadania jest napisanie kodu Terraforma, który utworzy infrastrukturę w wybranej chmurze - AWS lub Azure. Kod powinien składać się z definicji zasobów, takich jak instancje, sieci czy grupy bezpieczeństwa, które odpowiadają Twojemu projektowi.

Wymagania
Posiadanie konta w chmurze AWS lub Azure
Zainstalowany Terraform na lokalnej maszynie
Instrukcja
Sklonuj repozytorium na swój lokalny komputer
Przejdź do folderu z projektem
Skonfiguruj połączenie z Twoim kontem AWS lub Azure w pliku provider.tf używając odpowiednich wartości regionu i klucza API.
Uruchom polecenie terraform init, aby zainicjować projekt Terraforma
Następnie uruchom polecenie terraform plan, aby wygenerować plan zmian, które zostaną wprowadzone w infrastrukturze
Sprawdź, czy plan zmian jest zgodny z Twoimi oczekiwaniami, a następnie uruchom polecenie terraform apply, aby utworzyć infrastrukturę
Po zakończeniu działania programu, możesz zweryfikować utworzone zasoby w panelu konsoli AWS lub Azure.