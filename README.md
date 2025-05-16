# nosleguma_projekts
Programma, kas atgādina par mājas darbiem.
Šī ir Python programma, kura ir piemērota skolēniem/studentiem, kā arī citiem cilvēkiem jebkurā vecumā. 
Tas palīdz atcerēties savus majāsdarbus, parādot atgādinājumus norādītajā dienā un laikā.

## Projekta uzdevums:
Izveidot vienkāršu konsoles lietotni, kas:
Pirmkārt, ļauj pievienot mājasdarbus ar nosaukumu, dienu un laiku.
Otrkārt, saglabā tos `.json` failā, lai tie būtu pieejami arī pēc programmas pārstartēšanas.
Treškārt, atgādina par darbu īstajā dienā un laikā, izvadot paziņojumu terminālī.

## Izmantotas bibliotēkas
Programmas izstrādes laikā tiek izmantotas šādas Python bibliotēkas:
- `json` — ir saistīta ar datu saglabāšanu un ielāde visas datus `.json` failā.
- `datetime` — lai noteiktu tekošo datumu un laiku, un salīdzinātu tos ar darba datiem.
- `time` — lai iestatītu pauzes starp laika pārbaudēm.
- `threading` — lai atgādinājumu pārbaude darbotos fonā vienlaicīgi ar lietotāja ievadi.

## Pašdefinētās datu struktūras

Projektā ir izveidota pašdefinēta klase `MajasDarbs`, kas reprezentē vienu mājasdarbu:

class MajasDarbs:
    def __init__(self, nosaukums, diena, laiks):
        self.nosaukums = nosaukums
        self.diena = diena.capitalize()
        self.laiks = laiks

Ar šo klasi tiek saglabāti mājas darbu nosaukumi, diena, kad ir jāizpilda un precīzs laiks.

## Kā lietot šo programmu:
Instrukcija:
1. Ir jāpalaist izveidotu failu main.py ar Python
2. Pēc tam būs piedāvātas 3 izvēles:

Parādīt visus pievienotos darbus. -1
Pievienot jaunu darbu, ievadot nosaukumu, dienu un laiku. - 2
Iziet no programmas. - 3

3. Programma fonā nepārtraukti pārbauda, vai kādam darbam ir pienācis norādītais laiks, un izvada atgādinājumu terminālī.

Visi mājasdarbi būs saglabāti failā darbi.json. Pēc programmas pārstartēšanas šie dati automātiski tiek ielādēti un turpināti izmantot.

## Atgādinājuma mehānisms
Katru minūti programma pārbauda, vai tagadējais datums un laiks sakrīt ar kādu no mājasdarbiem.
Ja sakrīt, tad parādisies paziņojums:
Piemērs:
  Atgādinājums: Matemātikas darbs - Trešdien 15:00

## Ko varam vēl uzlabot
1. Izdarīt ta, lai programma atbalstītu vairākus atgādinājumus dienā.
Pašlaik programma var pievienot mājas darbus noteiktai dienai un vienam konkrētam laikam.

2. Pievienot iespēju dzēst vai labot esošos darbus.
Programmai tagad ir tikai divas funkcijas:
- Pievienot datus
- Skatīt visus datus

