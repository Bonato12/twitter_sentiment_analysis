import requests

bearer_token = 'AAAAAAAAAAAAAAAAAAAAAFY9owEAAAAA5N1wgcpARBFdenlLE0V%2F8NDr6aQ%3D7pzRccH530wX3HRrfESY3VOVFR1oPapfB3mlSJVldWAqyHusVS'

def create_headers(bearer_token):
    return {
        "Authorization": f"Bearer {bearer_token}",
    }

def get_tweet_by_id(headers, tweet_ids):
    url = "https://api.twitter.com/2/tweets"
    params = {
        "ids": ",".join(tweet_ids),  # Lista de IDs separados por coma
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

# Ejemplo de IDs de tweets para buscar
tweet_ids = ["1877489261898838098","1877437940395106661","1877522314452926655","1877523839967535119,1877404176298230164,1877411360897737055","1877426476338835904","1877352477546172486","1877464749333520387","1877180543739011563","1877047045648732577","1877468421194924185","1877426511667470640","1877558976247730625","1877558622961463554","1876855047306305783","1877558376076378365","1877558264377856050","1877554724712402972","1877556014783820237","1877560977442382045","1877560843337949286","1877560718511210596","1877560277132038221","1877559676692292003","1877558369864613984","1877556107494785191","1877555146009239660","1877554705942880475","1877551812011765996","1876009043409719659","1875744502176215343","1876118331197133211","1847348893404553472","1847381873309454414","1847349513729773570","1876626448695337216","1874247421682913450","1875357567893090694","1673693414561292297","1877366046652268941","1844521560821858451","1845591241783959745","1847792878707159355","1870452489478410584","1874988855482552397","1832193532607475816","1877053031381946774","1876037422636749133","1851676201552912445","1825268456410775720","1874821196279103818","1875663501345038746","1876998620748108193","1809986047574417521","1874214730220642741","1780424498497396795","1765761742490001842","1808545556261679337","1840108829872402632","1838024999543697442","1876758578737930527","1876797468572319796","1876754715347767630","1877730479392117129","1877680858384957940","1877691968098033976","1852198654947242050","1877650978553352208","1865179407045840972","1876724909348466916","1837992391707443625","1875004594436350034", "1876191593604251999","1877015748440182804","1877824111306584239" ,"1876490405149368489","1877729032776642718","1875064972251996397","1875636748451246299","1876693557341261864","1877384242637812182","1877023390822785048","1877538744993001910","1877345323854553325","1841513279023091831","1874511172919243127","1877057794987217326","1713887517160657191","1877728334752170027","1874289448969789834","1848129440003260864","1873700394645533001","1869688398111531476","1868163461018214777"] # Sustituir con IDs reales

print(len(tweet_ids))

headers = create_headers(bearer_token)
tweets = get_tweet_by_id(headers, tweet_ids)

print(len(tweets))

if 'data' in tweets:
    for tweet in tweets['data']:
        print(f"Tweet ID: {tweet['id']} - Texto: {tweet['text']}")
else:
    print("No se encontraron tweets o hubo un error:", tweets)


def probar():
    tweet_ids = [
        1877489261898838098, 1877437940395106661, 1877522314452926655, 1877523839967535119,
        1877404176298230164, 1877411360897737055, 1877426476338835904, 1877352477546172486,
        1877464749333520387, 1877180543739011563, 1877047045648732577, 1877468421194924185,
        1877426511667470640, 1877558976247730625, 1876855047306305783, 1877558376076378365,
        1877558264377856050, 1877554724712402972, 1877556014783820237, 1877560977442382045,
        1877560843337949286, 1877560718511210596, 1877560277132038221, 1877559676692292003,
        1877558369864613984, 1877556107494785191, 1877555146009239660, 1877554705942880475,
        1877551812011765996, 1876009043409719659, 1875744502176215343, 1876118331197133211,
        1847348893404553472, 1847381873309454414, 1847349513729773570, 1876626448695337216,
        1874247421682913450, 1875357567893090694, 1673693414561292297, 1877366046652268941,
        1844521560821858451, 1845591241783959745, 1847792878707159355, 1870452489478410584,
        1874988855482552397, 1832193532607475816, 1877053031381946774, 1876037422636749133,
        1851676201552912445, 1825268456410775720, 1874821196279103818, 1875663501345038746,
        1876998620748108193, 1809986047574417521, 1874214730220642741, 1780424498497396795,
        1765761742490001842, 1808545556261679337, 1840108829872402632, 1838024999543697442,
        1876758578737930527, 1876797468572319796, 1876754715347767630, 1877730479392117129,
        1877680858384957940, 1877691968098033976, 1852198654947242050, 1877650978553352208,
        1865179407045840972, 1876724909348466916, 1837992391707443625, 1875004594436350034,
        1876191593604251999, 1877015748440182804, 1877824111306584239, 1876490405149368489,
        1877729032776642718, 1875064972251996397, 1875636748451246299, 1876693557341261864,
        1877384242637812182, 1877023390822785048, 1877538744993001910, 1877345323854553325,
        1841513279023091831, 1874511172919243127, 1877057794987217326, 1713887517160657191,
        1877728334752170027, 1877728334752170027, 1874289448969789834, 1873700394645533001,
        1869688398111531476, 1868163461018214777, 1857049426885316988, 1873865611908194336,
        1877578595800912336, 1877741657128353972, 592046992769036289,  1275271079049691139,
        1869079304346452014, 1094840648472113153, 1847430319743332735, 1701330487896101224,
        1661381757629808642, 1825493704976609349, 1811000147909726486, 1873847770244931993,
        1871975945936261331, 1876133840785404216, 1876346836090490950, 1875305554580758706,
        1875043898705551794, 1876729024908558429, 1878254715156213781, 1878246720296960008,
        1878243244493996064, 1878195610672611543, 1878178913240731753, 1878906992447881460,
        1878759475336933516, 1877085113709691254, 1878556722404405366

    ]

    textos = [
        "🚨🇦🇷 ANDER HERRERA JUGARÁ EN BOCA JUNIORS.\nvía @Tato_Aguilera https://t.co/bFJ34IoI36",
        "Felicidades, @FranColapinto 👏\nNos vemos en Mayo! 😉 https://t.co/1CUrof3h4d",
        "CUMPLE EL SUEÑO DE SU VIDA… ES BOSTERO COMO NOSOTROS! 💙💛\nBIENVENIDO AL ÚNICO GRANDE, ANDER!  https://t.co/bOvFWTd47L",
        "@Labocatw QUE ALGUIEN LO PARE, FLORECHICHO ESTA DESACATADO https://t.co/feiwKAMszC",
        "FRANCO COLAPINTO ESTA EN CASA\nAAAAAAAAAAAAAAAAAAAAAAAAA ME VUELVO LOCO\n#Alpine https://t.co/ToLC5CPNUP https://t.co/SVTLMZx4ht",
        "Cuando manifiestas y se vuelve realidad 🙏🫶 https://t.co/sgSA8AitYp",
        "El machismo en la kings league. El presidente de argentina Markitos diciendo que le va comprar un seca platos a Natalia y Alana después de que anularan el gol del Kun. https://t.co/9rVnTlslW6",
        "Que los creadores de contenido de Pokémon en tiktok estéis haciendo un trend homófobo deja bien claro la poca creatividad que tenéis y lo rastreros que sois",
        '"Lo voy a demostrar con hechos". Nunca más Velasco en Independiente. https://t.co/vcJMD6KHo4',
        "Vergüenza ajena el quilombo entre Mauro Icardi, Wanda Nara y la China Suárez pero estoy así siguiendo todo lo que cuentan en los programas, Yanina Latorre y en las redes https://t.co/9awRcuWR4W",
        "Nunca olviden la opresión que se vive en Venezuela, Cuba y Nicaragua https://t.co/y3BYFHTGU1",
        "Ahora será rival, pero que el árbol no tape el bosque: en Europa le querían imponer a Schumacher, a Lawson o a Antonelli, y el se la jugó por Franco. Lo eligió, lo defendió a capa y espada y le dio la chance de su vida.\nGracias, tío James. Argentina será tu casa. https://t.co/E54hfMCQMF",
        "Siento que tío Flavio no le queda bien a Briatore. Creo que tiene más mística decirle nonno.\nEl nonno Flavio 🇮🇹🍝🤌🍕",
        "@eduardomenoni Hoy fue un mal día, lleno de errores y desorganización.",
        "a veces no me gusta ser tan sensible",
        "@camisand_ Mal dia, jueves :(",
        "Q mal q me senti todo el dia angina del orto😬",
        "A veces me cuestiono...\nqué haces ahí?\nHoy me siento triste, necesitaba un abrazo, a veces estamos rotos y preferimos ser prudentes y callar,\nBuena noche! 💤😴",
        "Soy yo o el día está insoportable\nMenos mal q ya termina",
        "cómo odio que ahora no se vean bien los links de spotify #RapeElonMusk",
        "t odio bida",
        "estoy cansado jefe https://t.co/B6WOawVh39",
        "Jajsjsjs ya estoy cansado de sentirme tan triste):",
        "que cansado q estoy",
        "Quiero dormir cansado, para no pensar en ti",
        "Que triste y cansado me siento 😔",
        "estoy cansado d pensar q es lo q va a pasar si mi mente se vuela un poco masssss",
        "@CaroTakk Me tienen cansado estos debiles mentales pendiente de la vida de los famosos.",
        "estado : enojado.",
        "nunca me ghostearon tanto en mi vida estoy indignado",
        "Me siento muy cansado y un poco frustrado la verdad. Que paja todo. No quiero verle la cara a nadie.",
        "Me siento tan frustrado",
        "Estoy muy triste y muy frustrado no se da nada.",
        "@dgtcsgo cabeza arriba pa sos buenisimo ❤️",
        "@dgtcsgo Ya van a salir las cosas, confianza.",
        "estoy puto frustrado soy un puto inútil q no se le da bien hacer nada q ganas de llorar y pegarme un balazo",
        "mi sueño frustrado es matarme",
        "q horrible es irse con ganas d quedarse",
        "Que horrible estar al final cadena alimenticia, todo trata de comerte https://t.co/4YrIevqPdd",
        "31° de máxima, que día horrible",
        '"Horrible partido. No se podía jugar al fútbol. Había que ir a la segunda pelota. No está bueno, pero es lo que toca. Las mejores condiciones son que haya un buen campo, un buen clima y que la pelota corra. No pedimos mucho".\n🗣️ Rodrigo De Paul. https://t.co/TjfUYrbpEj',
        "Toda esta semana he estado enfermo y la verdad, no saben qué horrible se siente",
        "Boca jugando de visitante es el San Marino del fútbol argentino. Es el equipo más horrible que existe.",
        "Los más lindo que hay https://t.co/59mML8TKhh",
        "todo es mas lindo cuando estamos los dos",
        "Que lindo vivir todo esto Un sueño Gracias 🇦🇷 por todo el cariño 🤍💙 https://t.co/N8s3jFHPFW",
        "Miércoles en el predio más lindo.  🌡️ 😏 https://t.co/JlSkfu7gYG",
        "Consejo: encuentren a alguien sano a quien querer, es lo más lindo de la vida. https://t.co/DyPYVx9RcV",
        "“El fútbol es el deporte más lindo y más sano del mundo, eso no le quepa la menor duda a nadie” ⚽ 🔟 ♾ https://t.co/oj0DxLDk63",
        "Te haces el lindo y estás hermoso mi amor",
        "estoy feliz con quien tengo a mi lado ahora",
        "Estoy feliz con lo que soy y con lo que tengo.",
        "Me pone sumamente contento que mi entretenimiento en la preadolescencia haya sido ver a dos gallegos jugando CoD y Minecraft. https://t.co/QWQ1Ua87RH",
        "panza llena, corazón contento… ahora si, a luchar contra el guason https://t.co/yhFtqcmEWh",
        "el es mi tío, se metió a una pileta por primera vez y está contento❤️ https://t.co/Qab37PLm1I",
        "Esta contento el loko https://t.co/R4KmWy3bbV",
        "🇦🇷🚨 Vélez decidió SEPARAR del plantel a Sebastián Sosa, Braian Cufré, José Florentín y Abiel Osorio tras una denuncia por abuso sexual radicada en Tucumán. https://t.co/S5I9kl5t3E",
        "🔥Confirmaron el procesamiento de Fernando Espinoza por abuso sexual\n✅ Quedó a un paso del juicio oral.\n➡️Kicillof lo sigue CUBRIENDO. https://t.co/wwvNBQBMwb",
        "el amor es un beso inesperado en la frente",
        "q ganas de dormir abrazada y q me digan, te amo  mi amor vamos a estar juntos toda la vida",
        "reírse como idiotas en la cama juntos es un lenguaje de amor",
        "me gusta el exceso de amor y atención",
        "Estas para hacer un mano a mano tomando fernet? Enviar",
        "@Zoramar1 Que tengas buen Viernes así como día🥰🥰",
        "Buen viernes. https://t.co/rdq1W21mT7",
        "Felicitaciones! Llegaste a otro viernes. Después de dos semanas cortas, haber sobrevivido esta semana larga tiene doble mérito. Salud!",
        "Gracias a dios es viernes",
        "Llegamos al viernes!!! Buen día 🙌🏼☀️😆🧉 https://t.co/hnJLFjSe8d",
        "Es viernes y Diego lo sabe 🍻 https://t.co/h88Cb2ivxh",
        "¡QUÉ REENCUENTRO! Paolo Goltz subió esta foto junto al Tano De Rossi. https://t.co/7covVaewOu",
        "Mañana es lunes de nuevo https://t.co/O2Q7ht5Oro",
        "estoy cansada de que me hagas llorar",
        "A veces llorar no es suficiente!",
        "ya no quiero llorar más",
        "Dejen de molestar con trabajo carajo, eso es hasta el lunes",
        "nunca sabrás lo que lloré esa noche",
        "Que asco me dan estos Kirchneristas, de defender a un dictador no se vuelve.\n https://t.co/PNVM7pBcll",
        "qué asco que normalicen las infidelidades, las mentiras y el dañar psicológicamente a una persona",
        "qué asco darse cuenta de tantas cosas🤢🤢",
        "no me estén vinculando con gente de mi pasado, me dan un chingo de asco",
        "Que te responda hasta la más mínima historia le suma mil puntos.",
        "Cuando apenas llevás 10 minutos en el trabajo y sabes que te faltan 9 horas para salir. https://t.co/W5t9IMWOsZ",
        "amo estar sola, amor tener casa sola, amo todo lo que tenga q ver con estar sola en paz",
        "Trabaja tanto en tu amor propio, que cuando llegue a tu vida alguien bueno a amarte de verdad, sientas que lo mereces.✨",
        "A mi nadie me va a hacer dudar de la excelente mujer que soy y del gran corazón que tengo.",
        "Cero resaca un 1 de enero. Excelente servicio.",
        "Los niños y las mascotas son una excelente combinación 🥰 https://t.co/vD6VBPyAgT",
        "Que tengan una excelente semana https://t.co/4Wpq43A0Uz",
        "Ongi etorri Ander, al club más grande del mundo. Jerarquía y calidad, otro excelente refuerzo https://t.co/vBbxEEg01b",
        "Ongi etorri Ander, al club más grande del mundo. Jerarquía y calidad, otro excelente refuerzo https://t.co/vBbxEEg01b",
        "🎆Que tengan un excelente inicio de año 2025🎇 https://t.co/GQ0GIFxIP0",
        "Es una atrás de la otra",
        "Bueno ya arrancamos mal!",
        "Totalmente pasado de rosca",
        "Quiero cabecear una bala",
        "era obvio q tenía que pasar una mierda para cerrar este año del ocote",
        "Qué bonito se siente cuando el corazón está contento.",
        "Andá a dormir chicho, que me hiciste la más feliz del mundo hoy.      (Recién empezaba el día, no?)",
        "Hay que estar felices porque locos ya estamos.",
        "Me alegraron mucho la noche",
        "Qué muchacho mágico",
        "¿Existirá algo más hermoso que la luna?",
        "LA LUNAAA❤️‍🔥",
        "Adicta al mate por",
        "Una mañana más triste no venía? 😔",
        "Bueno toca a agarrar la pala... Se acabó la joda...",
        "Cuando toca agarrar la pala de nuevo post feriado.... https://pbs.twimg.com/media/GSH3CZmWcAEbFp7?format=jpg&name=900x900",
        "Muy tibio maresca",
        "La cantidad de mantecol que comí en estos dos días por dios, soy un hombre feliz",
        "Mantente motivado pero sobre todo disciplinado.",
        "Estoy más motivado que nunca",
        "Estoy más motivado que nunca, voy por ese pinche sueño ☘️🙏🏽🙏🏽",
        "cumplí medio año en el gimnasio sin haber dejado en ningun momento y estoy más motivado q nunca",
        "que lindo coincidir humorísticamente con alguien",
        "Creo que me voy a enfermar de gripe :(",
        "Me voy a enfermar si sigo aquí 😮‍💨😮‍💨😮‍💨",
        "Tengo un ataque de ansiedad en plena calle 😭😭😭",
        "Me voy a enfermar de tanto ver el teléfono",
        "Me vengo a enfermar el último día la puta madre0",
        "Fo, que aspera va estar la semana",
        "[AHORA] En Palermo, chocó dos autos estacionados y volcó: está herido., https://x.com/i/status/1878759475336933516"
        "que miedo me da volver a pasar por lo mismo",
        "obsesionada con mejorar mi vida, me merezco todo! 🙌🏼🎀🎀🎀🎀🎀🎀",
        

    ]

    # Crear el dataframe
    df = pd.DataFrame({
        'Tweet ID': tweet_ids,
        'Texto': textos
    })

    # Mostrar el dataframe
    print(df)



