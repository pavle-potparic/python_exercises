import sqlite3

conn = sqlite3.connect('football_leagues.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS teams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    country_id INTEGER NOT NULL,
    FOREIGN KEY (country_id) REFERENCES countries(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    rating INTEGER NOT NULL,
    team_id INTEGER NOT NULL,
    FOREIGN KEY (team_id) REFERENCES teams(id)
)
''')

countries = ['England', 'Spain', 'Germany', 'France', 'Italy']
for country in countries:
    cursor.execute('INSERT OR IGNORE INTO countries (name) VALUES (?)', (country,))

teams_and_players = {
    'England': {
        'Manchester United': ['David de Gea', 'Aaron Wan-Bissaka', 'Harry Maguire', 'Victor Lindelof', 'Luke Shaw', 'Scott McTominay', 'Bruno Fernandes', 'Paul Pogba', 'Marcus Rashford', 'Ramsus Hojlund', 'Jadon Sancho'],
        'Liverpool': ['Alisson Becker', 'Trent Alexander-Arnold', 'Virgil van Dijk', 'Joel Matip', 'Andy Robertson', 'Fabinho', 'Jordan Henderson', 'Thiago Alcantara', 'Mohamed Salah', 'Sadio Mane', 'Roberto Firmino'],
        'Manchester City': ['Ederson', 'Kyle Walker', 'Ruben Dias', 'John Stones', 'Joao Cancelo', 'Rodri', 'Kevin De Bruyne', 'Phil Foden', 'Bernardo Silva', 'Gabriel Jesus', 'Raheem Sterling'],
        'Chelsea': ['Edouard Mendy', 'Reece James', 'Thiago Silva', 'Antonio Rudiger', 'Marcos Alonso', 'Jorginho', 'N’Golo Kante', 'Mason Mount', 'Kai Havertz', 'Christian Pulisic', 'Romelu Lukaku'],
        'Arsenal': ['Bernd Leno', 'Takehiro Tomiyasu', 'Ben White', 'Gabriel Magalhaes', 'Kieran Tierney', 'Thomas Partey', 'Granit Xhaka', 'Bukayo Saka', 'Emile Smith Rowe', 'Gabriel Martinelli', 'Pierre-Emerick Aubameyang'],
        'Tottenham Hotspur': ['Hugo Lloris', 'Emerson Royal', 'Cristian Romero', 'Eric Dier', 'Sergio Reguilon', 'Pierre-Emile Hojbjerg', 'Oliver Skipp', 'Lucas Moura', 'Heung-Min Son', 'Harry Kane', 'Dele Alli'],
        'Leicester City': ['Kasper Schmeichel', 'Timothy Castagne', 'Jonny Evans', 'Caglar Soyuncu', 'Luke Thomas', 'Wilfred Ndidi', 'Youri Tielemans', 'James Maddison', 'Harvey Barnes', 'Jamie Vardy', 'Kelechi Iheanacho'],
        'West Ham United': ['Lukasz Fabianski', 'Vladimir Coufal', 'Angelo Ogbonna', 'Kurt Zouma', 'Aaron Cresswell', 'Declan Rice', 'Tomas Soucek', 'Jarrod Bowen', 'Pablo Fornals', 'Said Benrahma', 'Michail Antonio'],
        'Everton': ['Jordan Pickford', 'Seamus Coleman', 'Michael Keane', 'Ben Godfrey', 'Lucas Digne', 'Abdoulaye Doucoure', 'Allan', 'Andros Townsend', 'Demarai Gray', 'Richarlison', 'Dominic Calvert-Lewin'],
        'Aston Villa': ['Emiliano Martinez', 'Matty Cash', 'Ezri Konsa', 'Tyrone Mings', 'Matt Targett', 'John McGinn', 'Douglas Luiz', 'Emiliano Buendia', 'Leon Bailey', 'Ollie Watkins', 'Danny Ings'],
        'Leeds United': ['Illan Meslier', 'Luke Ayling', 'Diego Llorente', 'Liam Cooper', 'Stuart Dallas', 'Kalvin Phillips', 'Mateusz Klich', 'Raphinha', 'Rodrigo', 'Jack Harrison', 'Patrick Bamford'],
        'Wolverhampton Wanderers': ['Jose Sa', 'Nelson Semedo', 'Conor Coady', 'Max Kilman', 'Romain Saiss', 'Joao Moutinho', 'Ruben Neves', 'Adama Traore', 'Daniel Podence', 'Francisco Trincao', 'Raul Jimenez'],
        'Newcastle United': ['Martin Dubravka', 'Javier Manquillo', 'Fabian Schar', 'Jamaal Lascelles', 'Jamal Lewis', 'Jonjo Shelvey', 'Isaac Hayden', 'Miguel Almiron', 'Allan Saint-Maximin', 'Callum Wilson', 'Joelinton'],
        'Crystal Palace': ['Vicente Guaita', 'Joel Ward', 'Joachim Andersen', 'Marc Guehi', 'Tyrick Mitchell', 'James McArthur', 'Conor Gallagher', 'Cheikhou Kouyate', 'Jordan Ayew', 'Wilfried Zaha', 'Christian Benteke'],
        'Southampton': ['Alex McCarthy', 'Tino Livramento', 'Jan Bednarek', 'Mohammed Salisu', 'Kyle Walker-Peters', 'Oriol Romeu', 'James Ward-Prowse', 'Stuart Armstrong', 'Nathan Redmond', 'Che Adams', 'Adam Armstrong'],
        'Burnley': ['Nick Pope', 'Matthew Lowton', 'James Tarkowski', 'Ben Mee', 'Charlie Taylor', 'Josh Brownhill', 'Ashley Westwood', 'Dwight McNeil', 'Johann Berg Gudmundsson', 'Chris Wood', 'Jay Rodriguez'],
        'Watford': ['Ben Foster', 'Kiko Femenia', 'Craig Cathcart', 'William Troost-Ekong', 'Danny Rose', 'Tom Cleverley', 'Moussa Sissoko', 'Juraj Kucka', 'Ismaila Sarr', 'Emmanuel Dennis', 'Joshua King'],
        'Norwich City': ['Tim Krul', 'Max Aarons', 'Ben Gibson', 'Grant Hanley', 'Brandon Williams', 'Kenny McLean', 'Billy Gilmour', 'Todd Cantwell', 'Kieran Dowell', 'Teemu Pukki', 'Milot Rashica'],
        'Brentford': ['David Raya', 'Sergi Canos', 'Pontus Jansson', 'Ethan Pinnock', 'Rico Henry', 'Christian Norgaard', 'Vitaly Janelt', 'Mathias Jensen', 'Bryan Mbeumo', 'Ivan Toney', 'Saman Ghoddos']
    },
    'Spain': {
        'Real Madrid': ['Thibaut Courtois', 'Daniel Carvajal', 'Eder Militao', 'David Alaba', 'Ferland Mendy', 'Casemiro', 'Luka Modric', 'Toni Kroos', 'Karim Benzema', 'Vinicius Junior', 'Rodrygo'],
        'Barcelona': ['Marc-Andre ter Stegen', 'Sergi Roberto', 'Gerard Pique', 'Ronald Araujo', 'Jordi Alba', 'Sergio Busquets', 'Frenkie de Jong', 'Pedri', 'Ousmane Dembele', 'Memphis Depay', 'Ferran Torres'],
        'Atletico Madrid': ['Jan Oblak', 'Kieran Trippier', 'Stefan Savic', 'Jose Gimenez', 'Renan Lodi', 'Marcos Llorente', 'Koke', 'Thomas Lemar', 'Angel Correa', 'Luis Suarez', 'Joao Felix'],
        'Sevilla': ['Yassine Bounou', 'Jesus Navas', 'Jules Kounde', 'Diego Carlos', 'Marcos Acuna', 'Fernando', 'Joan Jordan', 'Ivan Rakitic', 'Suso', 'Lucas Ocampos', 'Youssef En-Nesyri'],
        'Real Sociedad': ['Alex Remiro', 'Joseba Zaldua', 'Aritz Elustondo', 'Robin Le Normand', 'Nacho Monreal', 'Martin Zubimendi', 'Mikel Merino', 'David Silva', 'Adnan Januzaj', 'Mikel Oyarzabal', 'Alexander Isak'],
        'Villarreal': ['Geronimo Rulli', 'Juan Foyth', 'Raul Albiol', 'Pau Torres', 'Alfonso Pedraza', 'Dani Parejo', 'Etienne Capoue', 'Manu Trigueros', 'Gerard Moreno', 'Paco Alcacer', 'Samuel Chukwueze'],
        'Real Betis': ['Claudio Bravo', 'Hector Bellerin', 'German Pezzella', 'Marc Bartra', 'Alex Moreno', 'Guido Rodriguez', 'Sergio Canales', 'Nabil Fekir', 'Juanmi', 'Borja Iglesias', 'Cristian Tello'],
        'Athletic Bilbao': ['Unai Simon', 'Oscar de Marcos', 'Yeray Alvarez', 'Inigo Martinez', 'Yuri Berchiche', 'Unai Vencedor', 'Dani Garcia', 'Iker Muniain', 'Alex Berenguer', 'Inaki Williams', 'Raul Garcia'],
        'Celta Vigo': ['Matias Dituro', 'Hugo Mallo', 'Nestor Araujo', 'Jeison Murillo', 'Javi Galan', 'Renato Tapia', 'Brais Mendez', 'Denis Suarez', 'Franco Cervi', 'Iago Aspas', 'Santi Mina'],
        'Valencia': ['Jasper Cillessen', 'Jose Gaya', 'Gabriel Paulista', 'Omar Alderete', 'Thierry Correia', 'Carlos Soler', 'Hugo Guillamon', 'Uros Racic', 'Goncalo Guedes', 'Maxi Gomez', 'Denis Cheryshev'],
        'Espanyol': ['Diego Lopez', 'Oscar Gil', 'Leandro Cabrera', 'Sergi Gomez', 'Adria Pedrosa', 'Sergi Darder', 'Keidi Bare', 'Adrian Embarba', 'Oscar Melendo', 'Raul de Tomas', 'Wu Lei'],
        'Getafe': ['David Soria', 'Damian Suarez', 'Jorge Cuenca', 'Stefan Mitrovic', 'Mathias Olivera', 'Mauro Arambarri', 'Nemanja Maksimovic', 'Carles Alena', 'Jakub Jankto', 'Enes Unal', 'Jaime Mata'],
        'Granada': ['Luis Maximiano', 'Quini', 'German Sanchez', 'Domingos Duarte', 'Carlos Neva', 'Maxime Gonalons', 'Luis Milla', 'Ruben Rochina', 'Darwin Machis', 'Jorge Molina', 'Luis Suarez'],
        'Elche': ['Edgar Badia', 'Helibelton Palacios', 'Enzo Roco', 'Diego Gonzalez', 'Johan Mojica', 'Ivan Marcone', 'Gerard Gumbau', 'Fidel', 'Pere Milla', 'Lucas Boye', 'Javier Pastore'],
        'Osasuna': ['Sergio Herrera', 'Nacho Vidal', 'David Garcia', 'Aridane Hernandez', 'Juan Cruz', 'Lucas Torro', 'Jon Moncayola', 'Ruben Garcia', 'Kike Barja', 'Chimy Avila', 'Kike Garcia'],
        'Mallorca': ['Manolo Reina', 'Pablo Maffeo', 'Martin Valjent', 'Franco Russo', 'Jaume Costa', 'Iddrisu Baba', 'Salva Sevilla', 'Kang-in Lee', 'Takefusa Kubo', 'Dani Rodriguez', 'Abdon Prats'],
        'Alaves': ['Fernando Pacheco', 'Ximo Navarro', 'Victor Laguardia', 'Florian Lejeune', 'Ruben Duarte', 'Mamadou Loum', 'Tomas Pina', 'Edgar Mendez', 'Pere Pons', 'Joselu', 'Luis Rioja'],
        'Cadiz': ['Jeremias Ledesma', 'Iza Carcelen', 'Juan Cala', 'Fali', 'Alfonso Espino', 'Jens Jonsson', 'Fede San Emeterio', 'Salvi Sanchez', 'Alex Fernandez', 'Alvaro Negredo', 'Anthony Lozano'],
        'Rayo Vallecano': ['Stole Dimitrievski', 'Ivan Balliu', 'Alejandro Catena', 'Esteban Saveljich', 'Fran Garcia', 'Oscar Valentin', 'Santi Comesana', 'Isi Palazon', 'Alvaro Garcia', 'Randy Nteka', 'Radamel Falcao'],
        'Levante': ['Aitor Fernandez', 'Son', 'Rober Pier', 'Oscar Duarte', 'Carlos Clerc', 'Jose Campana', 'Nemanja Radoja', 'Gonzalo Melero', 'Jorge de Frutos', 'Roger Marti', 'Jose Luis Morales']
    },
    'France': {
        'Paris Saint-Germain': ['Gianluigi Donnarumma', 'Achraf Hakimi', 'Marquinhos', 'Presnel Kimpembe', 'Nuno Mendes', 'Leandro Paredes', 'Marco Verratti', 'Georginio Wijnaldum', 'Lionel Messi', 'Kylian Mbappe', 'Neymar'],
        'Marseille': ['Steve Mandanda', 'Pol Lirola', 'William Saliba', 'Duje Caleta-Car', 'Luan Peres', 'Valentin Rongier', 'Boubacar Kamara', 'Dimitri Payet', 'Cengiz Under', 'Arkadiusz Milik', 'Konrad de la Fuente'],
        'Lyon': ['Anthony Lopes', 'Leo Dubois', 'Jason Denayer', 'Jerome Boateng', 'Emerson Palmieri', 'Bruno Guimaraes', 'Houssem Aouar', 'Lucas Paqueta', 'Karl Toko Ekambi', 'Moussa Dembele', 'Xherdan Shaqiri'],
        'Monaco': ['Alexander Nubel', 'Ruben Aguilar', 'Axel Disasi', 'Benoit Badiashile', 'Caio Henrique', 'Aurelien Tchouameni', 'Youssouf Fofana', 'Gelson Martins', 'Aleksandr Golovin', 'Kevin Volland', 'Wissam Ben Yedder'],
        'Rennes': ['Alfred Gomis', 'Hamari Traore', 'Nayef Aguerd', 'Warmed Omari', 'Birger Meling', 'Flavien Tait', 'Baptiste Santamaria', 'Lovro Majer', 'Benjamin Bourigeaud', 'Martin Terrier', 'Gaetan Laborde'],
        'Lille': ['Ivo Grbic', 'Zeki Celik', 'Jose Fonte', 'Sven Botman', 'Reinildo Mandava', 'Benjamin Andre', 'Xeka', 'Jonathan Ikone', 'Jonathan Bamba', 'Burak Yilmaz', 'Jonathan David'],
        'Nice': ['Walter Benitez', 'Jordan Lotomba', 'Jean-Clair Todibo', 'Dante', 'Melvin Bard', 'Pablo Rosario', 'Mario Lemina', 'Calvin Stengs', 'Kasper Dolberg', 'Amine Gouiri', 'Justin Kluivert'],
        'Lens': ['Jean-Louis Leca', 'Jonathan Gradit', 'Kevin Danso', 'Facundo Medina', 'Jonathan Clauss', 'Seko Fofana', 'Yannick Cahuzac', 'Przemyslaw Frankowski', 'Gael Kakuta', 'Florian Sotoca', 'Ignatius Ganago'],
        'Strasbourg': ['Matz Sels', 'Frederic Guilbert', 'Alexander Djiku', 'Gerzino Nyamsi', 'Anthony Caci', 'Jeanricner Bellegarde', 'Sanjin Prcic', 'Adrien Thomasson', 'Ludovic Ajorque', 'Habib Diallo', 'Kevin Gameiro'],
        'Angers': ['Paul Bernardoni', 'Vincent Manceau', 'Ismael Traore', 'Romain Thomas', 'Souleyman Doumbia', 'Thomas Mangani', 'Nabil Bentaleb', 'Angelo Fulgini', 'Sofiane Boufal', 'Mohamed-Ali Cho', 'Stephane Bahoken'],
        'Montpellier': ['Jonas Omlin', 'Arnaud Souquet', 'Matheus Thuler', 'Mamadou Sakho', 'Mihailo Ristic', 'Jordan Ferri', 'Joris Chotard', 'Teji Savanier', 'Stephy Mavididi', 'Valere Germain', 'Elye Wahi'],
        'Reims': ['Predrag Rajkovic', 'Thomas Foket', 'Wout Faes', 'Yunis Abdelhamid', 'Konan', 'Marshall Munetsi', 'Moreto Cassama', 'Ilan Kebbal', 'Mathieu Cafaro', 'El Bilal Toure', 'Boulaye Dia'],
        'Brest': ['Gautier Larsonneur', 'Ronael Pierre-Gabriel', 'Brendan Chardonnet', 'Christophe Herelle', 'Jere Uronen', 'Haris Belkebla', 'Paul Lasne', 'Romain Faivre', 'Franck Honorat', 'Steve Mounie', 'Irvin Cardona'],
        'Bordeaux': ['Benoit Costil', 'Enock Kwateng', 'Laurent Koscielny', 'Mexer', 'Loris Benito', 'Otavio', 'Toma Basic', 'Yacine Adli', 'Remi Oudin', 'Hwang Ui-jo', 'Samuel Kalu'],
        'Nantes': ['Alban Lafont', 'Dennis Appiah', 'Andrei Girotto', 'Nicolas Pallois', 'Charles Traore', 'Pedro Chirivella', 'Mehdi Abeid', 'Ludovic Blas', 'Randal Kolo Muani', 'Moses Simon', 'Kalifa Coulibaly'],
        'Troyes': ['Gauthier Gallon', 'Issa Kabore', 'Jimmy Giraudon', 'Yoann Salmier', 'Giulian Biancone', 'Rominigue Kouame', 'Florian Tardieu', 'Xavier Chavalerin', 'Tristan Dingome', 'Mama Balde', 'Yoann Touzghar'],
        'Metz': ['Alexandre Oukidja', 'Fabien Centonze', 'Dylan Bronn', 'Boubakar Kouyate', 'Thomas Delaine', 'Habib Maiga', 'Pape Sarr', 'Farid Boulaya', 'Opa Nguette', 'Ibrahima Niane', 'Papa Yade'],
        'Clermont': ['Arthur Desmas', 'Akim Zedadka', 'Cedric Hountondji', 'Florent Ogier', 'Vital Nsimba', 'Johan Gastien', 'Jason Berthomier', 'Yohann Magnin', 'Jodel Dossou', 'Mohamed Bayo', 'Jim Allevinah'],
        'Saint-Etienne': ['Etienne Green', 'Mathieu Debuchy', 'Harold Moukoudi', 'Timothee Kolodziejczak', 'Miguel Trauco', 'Mahdi Camara', 'Yvan Neyou', 'Romain Hamouma', 'Denis Bouanga', 'Arnaud Nordin', 'Wahbi Khazri'],
        'Lorient': ['Paul Nardi', 'Houboulang Mendes', 'Julien Laporte', 'Andreaw Gravillon', 'Vincent Le Goff', 'Laurent Abergel', 'Fabien Lemoine', 'Enzo Le Fee', 'Yoane Wissa', 'Armand Lauriente', 'Terem Moffi']
    },
    'Germany': {
        'Bayern Munich': ['Manuel Neuer', 'Benjamin Pavard', 'Dayot Upamecano', 'Lucas Hernandez', 'Alphonso Davies', 'Joshua Kimmich', 'Leon Goretzka', 'Thomas Muller', 'Leroy Sane', 'Robert Lewandowski', 'Kingsley Coman'],
        'Borussia Dortmund': ['Gregor Kobel', 'Thomas Meunier', 'Mats Hummels', 'Manuel Akanji', 'Raphael Guerreiro', 'Axel Witsel', 'Jude Bellingham', 'Marco Reus', 'Julian Brandt', 'Erling Haaland', 'Donyell Malen'],
        'RB Leipzig': ['Peter Gulacsi', 'Nordi Mukiele', 'Willi Orban', 'Josko Gvardiol', 'Angelino', 'Kevin Kampl', 'Tyler Adams', 'Christopher Nkunku', 'Dani Olmo', 'Emil Forsberg', 'Andre Silva'],
        'Bayer Leverkusen': ['Lukáš Hrádecký', 'Jeremie Frimpong', 'Jonathan Tah', 'Edmond Tapsoba', 'Mitchell Bakker', 'Kerem Demirbay', 'Charles Aranguiz', 'Moussa Diaby', 'Florian Wirtz', 'Paulinho', 'Patrik Schick'],
        'Eintracht Frankfurt': ['Kevin Trapp', 'Danny da Costa', 'Martin Hinteregger', 'Evan N\'Dicka', 'Filip Kostić', 'Djibril Sow', 'Sebastian Rode', 'Daichi Kamada', 'Jesper Lindstrøm', 'Rafael Borré', 'Gonçalo Paciência'],
        'Borussia Monchengladbach': ['Yann Sommer', 'Stefan Lainer', 'Matthias Ginter', 'Nico Elvedi', 'Ramy Bensebaini', 'Denis Zakaria', 'Florian Neuhaus', 'Jonas Hofmann', 'Lars Stindl', 'Alassane Pléa', 'Marcus Thuram'],
        'VfL Wolfsburg': ['Koen Casteels', 'Kevin Mbabu', 'Maxence Lacroix', 'John Brooks', 'Paulo Otavio', 'Maximilian Arnold', 'Xaver Schlager', 'Josip Brekalo', 'Renato Steffen', 'Wout Weghorst', 'Lukas Nmecha'],
        'Hertha BSC': ['Alexander Schwolow', 'Dedryck Boyata', 'Niklas Stark', 'Jordan Torunarigha', 'Marvin Plattenhardt', 'Lucas Tousart', 'Santiago Ascacibar', 'Matheus Cunha', 'Vladimír Darida', 'Dodi Lukebakio', 'Krzysztof Piątek'],
        'SC Freiburg': ['Mark Flekken', 'Jonathan Schmid', 'Philipp Lienhart', 'Manuel Gulde', 'Christian Günter', 'Maximilian Eggestein', 'Nicolas Höfler', 'Vincenzo Grifo', 'Woo-yeong Jeong', 'Roland Sallai', 'Lucas Höler'],
        'VfB Stuttgart': ['Florian Müller', 'Konstantinos Mavropanos', 'Waldemar Anton', 'Marc Oliver Kempf', 'Borna Sosa', 'Atakan Karazor', 'Orel Mangala', 'Philipp Förster', 'Chris Führich', 'Omar Marmoush', 'Sasa Kalajdzic'],
        '1. FSV Mainz 05': ['Robin Zentner', 'Jeremiah St. Juste', 'Moussa Niakhaté', 'Stefan Bell', 'Silvan Widmer', 'Leandro Barreiro', 'Jean-Paul Boëtius', 'Dominik Kohr', 'Jae-sung Lee', 'Karim Onisiwo', 'Jonathan Burkardt'],
        '1899 Hoffenheim': ['Oliver Baumann', 'Kevin Akpoguma', 'Stefan Posch', 'Chris Richards', 'David Raum', 'Diadie Samassekou', 'Sebastian Rudy', 'Andrej Kramaric', 'Munas Dabbur', 'Christoph Baumgartner', 'Ihlas Bebou'],
        'FC Augsburg': ['Rafal Gikiewicz', 'Robert Gumny', 'Jeffrey Gouweleeuw', 'Felix Uduokhai', 'Iago', 'Carlos Gruezo', 'Rani Khedira', 'Daniel Caligiuri', 'André Hahn', 'Florian Niederlechner', 'Michael Gregoritsch'],
        '1. FC Köln': ['Timo Horn', 'Benno Schmitz', 'Rafael Czichos', 'Timo Hübers', 'Jannes Horn', 'Salih Özcan', 'Ellyes Skhiri', 'Ondrej Duda', 'Florian Kainz', 'Jan Thielmann', 'Anthony Modeste'],
        'Arminia Bielefeld': ['Stefan Ortega', 'Cedric Brunner', 'Amos Pieper', 'Joakim Nilsson', 'Anderson Lucoqui', 'Manuel Prietl', 'Sebastian Vasiliadis', 'Masaya Okugawa', 'Christian Gebauer', 'Fabian Klos', 'Janni Serra'],
        'VfL Bochum': ['Manuel Riemann', 'Cristian Gamboa', 'Armel Bella-Kotchap', 'Maxim Leitsch', 'Danilo Soares', 'Anthony Losilla', 'Robert Tesche', 'Gerrit Holtmann', 'Takuma Asano', 'Simon Zoller', 'Sebastian Polter'],
        'SpVgg Greuther Furth': ['Sascha Burchert', 'Marco Meyerhöfer', 'Nick Viergever', 'Maximilian Bauer', 'Jetro Willems', 'Sebastian Griesbeck', 'Paul Seguin', 'Jamie Leweling', 'Julian Green', 'Håvard Nielsen', 'Branimir Hrgota']
    },
    'Italy': {
        'Juventus': ['Wojciech Szczesny', 'Danilo', 'Leonardo Bonucci', 'Matthijs de Ligt', 'Alex Sandro', 'Weston McKennie', 'Arthur', 'Adrien Rabiot', 'Paulo Dybala', 'Alvaro Morata', 'Federico Chiesa'],
        'AC Milan': ['Mike Maignan', 'Davide Calabria', 'Fikayo Tomori', 'Alessio Romagnoli', 'Theo Hernandez', 'Franck Kessie', 'Ismael Bennacer', 'Sandro Tonali', 'Brahim Diaz', 'Zlatan Ibrahimovic', 'Olivier Giroud'],
        'Inter Milan': ['Samir Handanovic', 'Milan Skriniar', 'Stefan de Vrij', 'Alessandro Bastoni', 'Denzel Dumfries', 'Nicolo Barella', 'Marcelo Brozovic', 'Hakan Calhanoglu', 'Ivan Perisic', 'Lautaro Martinez', 'Edin Dzeko'],
        'AS Roma': ['Rui Patricio', 'Rick Karsdorp', 'Gianluca Mancini', 'Chris Smalling', 'Matias Vina', 'Bryan Cristante', 'Jordan Veretout', 'Lorenzo Pellegrini', 'Nicolo Zaniolo', 'Henrikh Mkhitaryan', 'Tammy Abraham'],
        'Napoli': ['David Ospina', 'Giovanni Di Lorenzo', 'Kalidou Koulibaly', 'Amir Rrahmani', 'Mario Rui', 'Fabian Ruiz', 'Piotr Zielinski', 'Eljif Elmas', 'Hirving Lozano', 'Victor Osimhen', 'Lorenzo Insigne'],
        'Lazio': ['Pepe Reina', 'Manuel Lazzari', 'Francesco Acerbi', 'Luiz Felipe', 'Adam Marusic', 'Lucas Leiva', 'Sergej Milinkovic-Savic', 'Luis Alberto', 'Felipe Anderson', 'Ciro Immobile', 'Pedro'],
        'Atalanta': ['Juan Musso', 'Rafael Toloi', 'Merih Demiral', 'Jose Luis Palomino', 'Davide Zappacosta', 'Marten de Roon', 'Remo Freuler', 'Joakim Maehle', 'Ruslan Malinovskyi', 'Duvan Zapata', 'Luis Muriel'],
        'Fiorentina': ['Bartlomiej Dragowski', 'Lorenzo Venuti', 'Nikola Milenkovic', 'Lucas Martinez Quarta', 'Cristiano Biraghi', 'Sofyan Amrabat', 'Gaetano Castrovilli', 'Giacomo Bonaventura', 'Jose Callejon', 'Dusan Vlahovic', 'Riccardo Sottil'],
        'Sassuolo': ['Andrea Consigli', 'Mert Muldur', 'Vlad Chiriches', 'Gian Marco Ferrari', 'Rogerio', 'Maxime Lopez', 'Davide Frattesi', 'Domenico Berardi', 'Filip Djuricic', 'Hamed Traore', 'Giacomo Raspadori'],
        'Verona': ['Ivor Pandur', 'Pawel Dawidowicz', 'Koray Gunter', 'Federico Ceccherini', 'Davide Faraoni', 'Ivan Ilic', 'Adrien Tameze', 'Darko Lazovic', 'Antonin Barak', 'Gianluca Caprari', 'Giovanni Simeone'],
        'Bologna': ['Lukasz Skorupski', 'Lorenzo De Silvestri', 'Adama Soumaoro', 'Gary Medel', 'Aaron Hickey', 'Mattias Svanberg', 'Nicolas Dominguez', 'Riccardo Orsolini', 'Roberto Soriano', 'Musa Barrow', 'Marko Arnautovic'],
        'Torino': ['Vanja Milinkovic-Savic', 'Wilfried Singo', 'Bremer', 'Koffi Djidji', 'Cristian Ansaldi', 'Sasa Lukic', 'Tommaso Pobega', 'Karol Linetty', 'Josip Brekalo', 'Antonio Sanabria', 'Andrea Belotti'],
        'Udinese': ['Marco Silvestri', 'Nahuel Molina', 'Rodrigo Becao', 'Bram Nuytinck', 'Jens Stryger Larsen', 'Tolgay Arslan', 'Walace', 'Roberto Pereyra', 'Gerard Deulofeu', 'Ignacio Pussetto', 'Beto'],
        'Sampdoria': ['Emil Audero', 'Bartosz Bereszynski', 'Omar Colley', 'Julian Chabot', 'Tommaso Augello', 'Albin Ekdal', 'Morten Thorsby', 'Antonio Candreva', 'Manolo Gabbiadini', 'Francesco Caputo', 'Fabio Quagliarella'],
        'Genoa': ['Salvatore Sirigu', 'Davide Biraschi', 'Andrea Masiello', 'Domenico Criscito', 'Stefano Sabelli', 'Nicolo Rovella', 'Milan Badelj', 'Hernani', 'Goran Pandev', 'Caleb Ekuban', 'Mattia Destro'],
        'Spezia': ['Jeroen Zoet', 'Kelvin Amian', 'Petko Hristov', 'Martin Erlic', 'Simone Bastoni', 'Jacopo Sala', 'Giulio Maggiore', 'Emmanuel Gyasi', 'Viktor Kovalenko', 'Daniele Verde', 'Rey Manaj'],
        'Cagliari': ['Alessio Cragno', 'Gabriele Zappa', 'Diego Godin', 'Andrea Carboni', 'Charalampos Lykogiannis', 'Kevin Strootman', 'Razvan Marin', 'Nahitan Nandez', 'Joao Pedro', 'Keita Balde', 'Leonardo Pavoletti'],
        'Venezia': ['Niki Maenpaa', 'Pasquale Mazzocchi', 'Mattia Caldara', 'Pietro Ceccaroni', 'Ridgeciano Haps', 'Luca Fiordilino', 'Gianluca Busio', 'Dor Peretz', 'Mattia Aramu', 'David Okereke', 'Thomas Henry'],
        'Empoli': ['Guglielmo Vicario', 'Petar Stojanovic', 'Ardian Ismajli', 'Sebastiano Luperto', 'Fabiano Parisi', 'Samuele Ricci', 'Leo Stulac', 'Filippo Bandinelli', 'Nedim Bajrami', 'Patrick Cutrone', 'Andrea Pinamonti'],
        'Salernitana': ['Vid Belec', 'Nadir Zortea', 'Stefan Strandberg', 'Norbert Gyomber', 'Wajdi Kechrida', 'Lassana Coulibaly', 'Francesco Di Tacchio', 'Grigoris Kastanos', 'Simy', 'Federico Bonazzoli', 'Milan Djuric']
    }
}

for country, teams in teams_and_players.items():
    cursor.execute('SELECT id FROM countries WHERE name = ?', (country,))
    country_id = cursor.fetchone()[0]

    for team, players in teams.items():
        cursor.execute('INSERT INTO teams (name, country_id) VALUES (?, ?)', (team, country_id))
        team_id = cursor.lastrowid

        for player in players:
            cursor.execute('INSERT INTO players (name, team_id) VALUES (?, ?)', (player, team_id))

conn.commit()
conn.close()
