def vigenere(
        text: str, key: str, 
        alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
        encrypt=True
):
    result = ''

    for i in range(len(text)):
        letter_n = alphabet.index(text[i])
        key_n = alphabet.index(key[i % len(key)])
        if encrypt:
            value = (letter_n + key_n) % len(alphabet)
        else:
            value = (letter_n - key_n) % len(alphabet)
        #если мы меняем -а- на -б- то "-1"
        result += alphabet[value-1]

    return result

def vigenere_encrypt(text, key):
    return vigenere(text=text, key=key, encrypt=True)

def vigenere_decrypt(text, key):
    return vigenere(text=text, key=key, encrypt=False)

al = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
gls = "аеёиоуыэюя"
rr = []

uu = len(al)

y =0
y1=0 
i=0
otvet = ""
otv4 = []
uuu = uu-1

while i < uu:
  ii =0
  while ii < uu:
    iii=0
    while iii < uu:
      iiii=0
      while iiii < uu:
        
        #исключаем несуществующие слова
        if ("ь" == al[i]) or ("ъ" == al[i]) or ("ъ" == al[iii]) or ("ъ" == al[iiii]) or ("ы" == al[i]) or (al[i] == al[ii]) or (al[i] == al[ii] == al[iii]) or (al[i] == al[ii] == al[iii] == al[iiii]) or (gls.find(al[i])!= -1 and gls.find(al[ii]) != -1 and gls.find(al[iii]) != -1) or (gls.find(al[ii])!= -1 and gls.find(al[iii]) != -1 and gls.find(al[iiii]) != -1) or (gls.find(al[i])!= -1 and gls.find(al[ii]) != -1 and gls.find(al[iii]) != -1 and gls.find(al[iiii]) != -1) or (gls.find(al[i])== -1 and gls.find(al[ii]) == -1 and gls.find(al[iii]) == -1) or (gls.find(al[ii])== -1 and gls.find(al[iii]) == -1 and gls.find(al[iiii]) == -1) or (gls.find(al[i])== -1 and gls.find(al[ii]) == -1 and gls.find(al[iii]) == -1 and gls.find(al[iiii]) == -1):
          y1+=1
        else:
          b=1
          otv4.append(str(al[i]+al[ii]+al[iii]+al[iiii]) +".\n"+vigenere_decrypt("южэньлчубрюжэюевызьйэхюжсфшцвзьйгтаесофтшвбусуфсфрэутсяхфжяхшввновсрозвцолэщюуьеёлопюхюхпвсффусафчюхьлашфхбдэгъеяошжпзвцоляхфсрхпкгйвфоцясьуиянхпкэуюдаечркъвзетшъфцъленяуюзагьсэюецазуцвеюьфешиэсжчюфаечешчшзьтпцжтюхфъэлжйбнюзютаутуфцбгьнассущуктюнбхфжбчслэщюуьевлчеёлшжкъшцылвйыяэущтфхшчфхшмэущфяйёлпрлрюошнюсьцэнъгёнюрэущхфъэлънпхппцзяхюёаеьпэаелэщюуьеёлютэюенбзажшфэаефайуфвжрюбчасаебышхозвцолундчфхфрёнацфчбвпмэгжнвпэуцгвцоепхшгэчкеюмьсцткшайззэнщеюёыгбчшчюхьлаусгэнохфъэсыутлжйбнюобуфикфдйаююёагрувншнэчюхьгёнш",al[i]+al[ii]+al[iii]+al[iiii]) + "\n\n")
        y+=1
        iiii+=1
      iii+=1
    ii+=1
  i+=1

i=0
otv3 = []
y3_include = 0
y3_elements = 0
while i < uu:
  ii =0
  while ii < uu:
    iii=0
    while iii < uu:
      #исключаем несуществующие слова
      if ("ь" == al[i]) or ("ъ" == al[i]) or ("ъ" == al[iii]) or ("ы" == al[i]) or (al[i] == al[ii] == al[iii]) or (al[i] == al[ii]) or (gls.find(al[i])!= -1 and gls.find(al[ii]) != -1 and gls.find(al[iii]) != -1) or (gls.find(al[i])== -1 and gls.find(al[ii]) == -1) or (gls.find(al[i])== -1 and gls.find(al[ii]) == -1 and gls.find(al[iii]) == -1):
          y3_include+=1
      else:
        b=1
        #otv3.append(str(al[i]+al[ii]+al[iii]) +".\n"+vigenere_decrypt("фустёъяесщёъхсмойфгчхлйъчпэпбглпърпцфйюхёщютчсссзгюздыдфрзуоювэгомтпмрбшсдхлтыфустёъяярзчсруэгмхкбглйъгрэзеьуйлхйхжсаёйвчфънчхмлэснсхппсгмйоызиъгшсрйслнсзуаупозоищёъхсмойфгчхлпюрпорьвеьдлтшлусоэъюцьупгзеаубяглузрэлолхблппрзмисспгохкбглйхцрэггшзохввмкбщлемрозшгздпэтпюхбоьйчгюшзнсруыеусшоыопплшсфлымтэзезхпузважёясрэзесожърбыфоыеёыдъхшрэзеюхбооёълкытфявцэзщсрйлфуывъхшрсуёртссжрэлаялёщкбргшоювыутэзеюхгхрхыунмхйфгчхлешвсмкгххйллобссщгчхсоъюцюлтязнхкоыеьвтссжмыйёълкьстяггёллыейшлйфцзстсхффяфуоцяёлцъгсзрлслирзмхмпюцъсфуооасхтлнбчтсмейшсрыхпщцлэлусуйккомъёълёчсуыуппсомлвыоёстпшрпыхсмйбсхсыоэхрхыунмхйфгчхл",al[i]+al[ii]+al[iii]) + "\n\n")
      y3_elements+=1
      iii+=1
    ii+=1
  i+=1


f = open( 'key-anr-result.txt', 'w' )
f.write("".join(otv4))

print(y)
print(str(y1) + " -4-исключения-")
print(str(y3_include) + " -3-исключения-")
print(str(y3_elements) + " -3-все элементы-")
#print("".join(otv))

print("\n проверка рассшифровки 1")
print(vigenere_decrypt("рээёщяохснфёчнмякыфбшоаббытдёгшккаъьтэрнкщввтччюфьвжцэсефцуудбэвзйфвжифюшйшьысажхюкеуубюфълюоышюфьвжцоььзэчафхэофюфдёешьияггхчавзщшюфырьучавзоэьечюфаууьууэьерашнвыпшовшхэыжэонёчнтдщюяуфпйшрбюхчэбёёрэвпщюбшвабфркэрээёщяявчъфвхуауьчшццвягояюхрчъумткэрээёщябвыяпбеувезэшезэщешрпьхяшбётышмоиькуьжщцыохэбякэяшцоёьощюажчэьцэсуучоефавузьюэрээёщяядоэрдкбпшшьюхбубхфшбёзо","енот"))

print("\n проверка рассшифровки 2")
print(vigenere_decrypt("щбфщбнчучи","зал"))
