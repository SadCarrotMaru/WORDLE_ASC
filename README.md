# WORDLE_ASC 
Membrii echipă: <br />
  ~ Crânganu Denisa Mariana  <br />
  ~ Brabete Marius Stelian   <br />
  ~ Pîrvulescu Daria Maria  <br />
  ~ Buzatu Giulian  <br />
Medie încercări: 4.00786  <br />
Pentru a juca, se executa wordle.py. <br />

Conținut proiect: <br />
  Proiectul nostru contine 2 programe principale:   <br />
    ⬤: wordle.py care este jocul wordle principal si contine: <br />
            ~ interfata <br />
            ~ user_input (atat de la tastatura, cat si de la mouse) <br />
            ~ sageti pentru deplasarea prin cuvintele incercate <br />
            ~ multi-threading (pentru a rula programul de a calcula cele mai bune cuvinte pentru a castiga jocul, programele comunica prin 2 fisiere situate in folderul tmp) <br />
    ⬤: bot.exe care este calculatorul de entropie, avand inclus in el structures.cpp pentru a fi mai vizibil codul in timpul lucrului in echipa: <br />
            ~ pentru calculul entropiei, retinem doua structuri, m si full_database. (m este lista care contine cuvintele care inca pot fi castigatoare, iar full_database contine toate cuvintele din fisier) <br />
            ~ pentru fiecare cuvant din full_database calculam entropia (deoarece un cuvant care nu poate fi castigator poate avea o entropie mai mare), folosindu-ne de configuratiile care rezulta daca ele ar fi jucate <br />

Imagini proiect: <br />
![image](https://user-images.githubusercontent.com/85646597/204155465-b7347f5b-6f70-409d-aacf-c49f5a9c7241.png)
![image](https://user-images.githubusercontent.com/85646597/204155472-89a259cc-e2f0-4511-b840-249f82c36a82.png)
![image](https://user-images.githubusercontent.com/85646597/204155477-43bd4b44-5538-47f7-b0fa-07e936837120.png)

        

Documentație:  <br />
https://stackoverflow.com/questions/13445688/how-to-generate-a-random-number-in-c <br />
https://github.com/baraltech/Wordle-PyGame   <br />
https://docs.python.org/3/library/os.html     <br />
https://www.pygame.org/docs/      <br />
https://www.youtube.com/watch?v=v68zYyaEmEA   <br />
https://docs.python.org/3/library/subprocess.html <br />
https://stackoverflow.com/questions/28284715/python-subprocess-popen-wait-for-completion <br />

![image](https://user-images.githubusercontent.com/85646597/204140146-e368b2a3-5252-4c27-b9ce-3b5242ac9c8a.png)
