library(shiny)
library(plotly)
library(ggplot2)

# App is created in Slovak Language
ui <- fluidPage(theme = "mytheme.css",
                tabsetPanel(
                  tabPanel(
                    title = "Domov",
                    # Description of App
                    sidebarLayout( position = "right",
                                   sidebarPanel(
                                     span("Dáta sú použité zo stránky"), 
                                     strong("http://www.hockeyabstract.com"),
                                     br(),
                                     br(),
                                     br(),
                                     div("V tejto aplikácii sa zameriavame na predikovanie platov hráčov NHL na základe štatistík zo 7 predchádzajúcich sezón, celý popis dát aj s vysvetlivkami je popísaný na obrazovke: ", strong("ATRIBÚTY."), 
                                         "Postupne vyberáme najvhodnejšie atribúty pre analýzu dát, zobraziť sa dáta dajú na obrazovke: ", strong("VIZUALIZÁCIA."), 
                                         "Následne vytvárame viacero modelov pomocou ktorých predikujeme pravdepodobný plat hráča, výsledky zo všetkým modelom sa dajú zobraziť na obrazovke: ", strong("MODEL."),
                                         "A pomocou toho najvhodnejšieho modelu podľa nás vypočítavame reálne predpokladaný plat hráča, sami si to môžete vyskúšať na obrazovke: ", strong("VÝPOČET."))
                                   ),#sidebarPanel
                                   mainPanel(
                                     h1(strong("Vitajte v aplikácii Stats ProHockey,"), align = "center"),
                                     h3(strong("analyzujeme štatistiky z NHL"), align = "right"),
                                     img(src = "SPH2.png", align = "right", height = 500, width = 650)
                                   )#mainPanel
                    )#sidebarLayout
                  ),#tabPanel
                  
                  tabPanel(
                    title = "Atribúty",
                    #Description of Attributes
                    wellPanel(titlePanel("Kompletná tabuľka štatistík a význam atribútov"),
                    div(strong("Názov štatistiky - Popis štatistiky - v zátvorke pre ktoré dáta platia štatistiky"), style = "color:green"),
                    div("Ak pri štatistiky nie je žiadna zátvorka znamená to, že štatistika sa používa u oboch typoch dát", style = "color:grey"),
                    br()),
                    sidebarPanel(
                      p(strong("Spoločné atribúty"), style = "font-size: 20px"),
                    br(),
                    p(strong("CapHit"), " - Plat hráča - Cieľový atribút", style = "color:green"),
                    p(strong("FirstName "), " - Krstné Meno"),
                    p(strong("LastName "), " - Priezvisko"),
                    p(strong("DOB "), " - Dátum narodenia"),
                    p(strong("Ctry"), " - Krajina"),
                    p(strong("HT"), " - Váha"),
                    p(strong("Wt"), " - Výška"),
                    p(strong("Team"), " - Tím"),
                    p(strong("Status"), " - Typ zmluvy hráčov - UFA/RFA"),
                    p(strong("Season"), " - Sezóna")),
                    sidebarPanel(
                      p(strong("Brankárske atribúty"), style = "font-size: 20px"),
                    br(),
                    p(strong("C"), " - Ruka(brankár)"),
                    p(strong("GS"), " - Počet zápasov(brankár)"),
                    p(strong("W"), " - Výhry(brankár)"),
                    p(strong("L"), " - Prehry(brankár)"),
                    p(strong("OT"), " - Prehry po predĺžení(brankár)"),
                    p(strong("SA"), " - Strely na brankára(brankár)"),
                    p(strong("SV"), " - Zásahy(brankár)"),
                    p(strong("GAA"), " - Priemer gólov na zápas(brankár)"),
                    p(strong("SV."), " - Úspešnosť zásahov(brankár)"),
                    p(strong("GR"), " - Počet zápasov ako druhý brankár(brankár)"),
                    p(strong("PIM"), " - Trestné minúty(brankár)"),
                    p(strong("MIN"), " - Odohrané minúty(brankár)"),
                    p(strong("SO"), " - Čisté konto(brankár)"),
                    p(strong("StGA"), " - Inkasované góly ako prvý brankár(brankár)"),
                    p(strong("StSV"), " - Strely ako prvý brankár(brankár)"),
                    p(strong("StMIN"), " - Minúty ako prvý brankár(brankár)"),
                    p(strong("StSV."), " - Úspešnosť zásahov ako prvý brankár(brankár)"),
                    p(strong("StGAA"), " - Priemer gólov ako prvý brankár(brankár)"),
                    p(strong("QS"), " - Kvalitné štarty - Úspšnosť zásahov nad 90%(brankár)"),
                    p(strong("QS."), " - Početnosť kvalitných štartov(brankár)"),
                    p(strong("ReGA"), " - Inkasované góly ako druhý brankár(brankár)"),
                    p(strong("ReSV"), " - Strely ako druhý brankár(brankár)"),
                    p(strong("ReMIN"), " - Minúty ako druhý brankár(brankár)"),
                    p(strong("ReGAA"), " - Priemer gólov ako druhý brankár(brankár)"),
                    p(strong("ReSV."), " - Úspešnosť zásahov ako druhý brankár(brankár)"),
                    p(strong("GPS"), " - Body získané výkonom brankára(brankár)"),
                    p(strong("ESA"), " - Strely pri rovnakom počte hráčov na ľade(brankár)"),
                    p(strong("ESSV."), " - Úspešnosť zásahov pri rovnakom počte hráčov na ľade(brankár)"),
                    p(strong("SHSA"), " - Strely v oslabení(brankár)"),
                    p(strong("SHSV."), " - Úspešnosť zásahov v oslabení(brankár)"),
                    p(strong("PPSA"), " - Strely v presilovke(brankár)"),
                    p(strong("PPSV."), " - Úspešnosť zásahov v presilovke(brankár)"),
                    p(strong("SOW"), " - Výhry v samostatných nájazdoch(brankár)"),
                    p(strong("SOL"), " - Prehry v samostatných nájazdoch(brankár)"),
                    p(strong("SSA"), " - Strely v samostatných nájazdoch(brankár)"),
                    p(strong("SGA"), " - Góly v samostatných nájazdoch(brankár)"),
                    p(strong("SOSV."), " - Úspešnosť zásahov v samostatných nájazdoch(brankár)")),
                    sidebarPanel(
                      p(strong("Hráčske atribúty"), style = "font-size: 20px"),
                    br(),
                    p(strong("Pos"), " - Pozícia hráča(hráč)"),
                    p(strong("S"), " - Ruka(hráč)"),
                    p(strong("TOI"), " - Čas na ľade(hráč)"),
                    p(strong("TOI.G"), " - Čas na ľade na zápas(hráč)"),
                    p(strong("GP"), " - Zápasy(hráč)"),
                    p(strong("G"), " - Góly(hráč)"),
                    p(strong("G/G"), " - Góly na zápas(hráč)"),
                    p(strong("A"), " - Asistencie(hráč)"),
                    p(strong("A/G"), " - Asistencie na zápas(hráč)"),
                    p(strong("Pts"), " - Body(hráč)"),
                    p(strong("Pts/G"), " - Body na zápas(hráč)"),
                    p(strong("+/-"), " - Hodnotenie +/-(hráč)"),
                    p(strong("PIM"), " - Trestné minúty(hráč)"),
                    p(strong("PIM/G"), " - Trestné minúty na zápas(hráč)"),
                    p(strong("Shifts"), " - Striedania(hráč)"),
                    p(strong("Shifts/G"), " - Striedania na zápas(hráč)"),
                    p(strong("Sh"), " - Strely(hráč)"),
                    p(strong("Sh/G"), " - Strely na zápas(hráč)"),
                    p(strong("Sh."), " - Úspešnosť streľby(hráč)"),
                    p(strong("MsS"), " - Nepresné strely(hráč)"),
                    p(strong("OPS"), " - Ofenzívne body tímu(hráč)"),
                    p(strong("DPS"), " - Defenzívne body tímu(hráč)"),
                    p(strong("PS"), " - Získane body tímu(hráč)"),
                    p(strong("Match"), " - Trestné strieľania v zápase(hráč)"),
                    p(strong("Misc"), " - Tresty v zápase(hráč)"),
                    p(strong("G Misc"), " - Tresty na zápas(hráč)"),
                    p(strong("PDO"), " - Ofenzívna a defenzívna úspšnosť(hráč)"),
                    p(strong("Corsi"), " - Strely na bránu, zblokované strely, nepresné strely(hráč)"),
                    p(strong("RelC"), " - Relatívne Corsi(hráč)"),
                    p(strong("GvA"), " - Straty pukov(hráč)"),
                    p(strong("TkA"), " - Zisky pukov(hráč)"),
                    p(strong("Diff"), " - TkA-GvA(hráč)"),
                    p(strong("Diff/G"), " - Diff na zápas(hráč)"),
                    p(strong("Blocked"), " - Zblokované strely(hráč)"),
                    p(strong("Bl/G"), " - Zblokované strely na zápas(hráč)"),
                    p(strong("Hits"), " - Hity(hráč)"),
                    p(strong("Hits/G"), " - Hity na zápas(hráč)"),
                    p(strong("FO."), " - Úspešnosť na vhadzovaniach(hráč)"),
                    p(strong("FOW"), " - Vyhrané vhadzovania(hráč)"),
                    p(strong("FOL"), " - Prehrané vhadzovania(hráč)"),
                    p(strong("FG"), " - Prvé góly v zápase(hráč)"),
                    p(strong("GWG"), " - Víťazné góly(hráč)"),
                    p(strong("OTG"), " - Góly v predĺžení(hráč)"),
                    p(strong("ENG"), " - Góly do prázdnej brány(hráč)"),
                    p(strong("PSG"), " - Góly z trestných strieľaní(hráč)"),
                    p(strong("AdvG"), " - FG+GWG+OTG(hráč)"),
                    p(strong("RelG"), " - G-ENG-PSG(hráč)"),
                    p(strong("SOS"), " - Strely v samostatných nájazdoch(hráč)"),
                    p(strong("SOG"), " - Góly v samostatných nájazdoch(hráč)")
                  )),
                  
                  tabPanel(
                    title = "Vizualizácia",
                    #Basic visualization of data
                    sidebarLayout(position = "right",
                      sidebarPanel(
                        wellPanel(strong("Obrazovka slúži na zobrazenie dát"), style = "background: #627cef; color:white; font-size: 20px"),
                        selectInput("Data", "Vyberte si prosím dáta z menu", choices = c("Defenseman-UFA","Defenseman-RFA", "Defenseman-Rookie", "Forward-UFA", "Forward-RFA", "Forward-Rookie", "Goalies-UFA", "Goalies-RFA", "Goalies-Rookie"), selected = "Forward-UFA"),
                        code("Vysvetlivky"),
                        br(),
                        strong("RFA - Obmedzený voľný hráč"),
                        br(),
                        strong("UFA - Neobmedzený voľný hráč"),
                        br(),
                        strong("Rookie - Nováčik"),
                        br()
                      ),
                      mainPanel(
                        plotlyOutput("plot"),
                        wellPanel(span(htmlOutput("Text"),style= "color:darkblue; font-size: 15px"))
                      )
                      )
                    ),
                  
                  tabPanel(
                    title = "Model",
                    #Description of models
                    sidebarLayout(position = "right",
                      sidebarPanel(
                        wellPanel(strong("Obrazovka slúži na porovnanie viacerých modelov"), style = "background: #627cef; color:white; font-size: 20px"),
                        radioButtons("Model", "Vyberte si jeden z modelov", choices = c("Feature Selection","Stepwise Regression", "Polynomial Regression"), selected = "Feature Selection"),
                        em("Na obrazovke máme možnosť sledovať výsledky z vybraných modelov")
                        ),
                      mainPanel(
                        wellPanel(span(htmlOutput("Text2"),style= "color:darkblue; font-size: 15px")),
                        wellPanel(dataTableOutput("table"))
                        )
                      )
                    ),
                  
                  tabPanel(
                    #Salary calculation in the chart
                    title = "Výpočet",
                    sidebarLayout(position = "right",
                      sidebarPanel(
                        wellPanel(strong("Obrazovka slúži na výpočet platu"), style = "background: #627cef; color:white; font-size: 20px"),
                        br(),
                        p("Graf vznikol použitím polynomiálnej regresie, ktorá bola počítaná špeciálne pre každý z datových súborov, následne tieto výsledky boli priradené do jednej tabuľky a vybraný z nej hráči hrajúci v sezóne 17/18."),
                        br(),
                        selectInput("Meno", "Vyberte si ľubovoľného hráča", choices = c("", Name), selected = ""),
                        br(),
                        actionButton("OK", "OK", style = "background: #627cef; color:white; font-size: 20px")
                        ),
                      mainPanel(
                        plotOutput("model"),
                        wellPanel(em("Na grafe vidíme zobrazený reálny plat a predikovaný plat zvoleného hráča"))
                      )
                    )
                  )
))

server <- function(input, output) {
  
  output$plot = renderPlotly({
    #Graph output in Visualization
    if (input$Data == "Defenseman-Rookie"){
      plot_ly(DefensemanN, 
              x = ~CapHit, 
              y = ~TOI.G, color = ~Hits.G, size = ~Pts.G, 
              text = ~paste(First.Name,Last.Name, "(", Ctry, ")", "-", Team, Season), 
              colors = c("blue", "red" ,"orange", "green", "yellow"))
    }
    else if (input$Data == "Defenseman-UFA"){
      plot_ly(DefensemanU, 
              x = ~CapHit, 
              y = ~TOI.G, color = ~Hits.G, size = ~Pts.G, 
              text = ~paste(First.Name,Last.Name, "(", Ctry, ")", "-", Team, Season), 
              colors = c("blue", "red" ,"orange", "green", "yellow"))
    }
    else if (input$Data == "Defenseman-RFA") {
      plot_ly(DefensemanR, 
              x = ~CapHit, 
              y = ~TOI.G, color = ~Hits.G, size = ~Pts.G, 
              text = ~paste(First.Name,Last.Name, "(", Ctry, ")", "-", Team, Season), 
              colors = c("blue", "red" ,"orange", "green", "yellow"))
    }
    else if (input$Data == "Forward-Rookie") {
      plot_ly(ForwardN, 
              x = ~CapHit, 
              y = ~TOI.G, color = ~Sh.G, size = ~Pts.G, 
              text = ~paste(First.Name,Last.Name, "(", Ctry, ")", "-", Team, Season), 
              colors = c("blue", "red" ,"orange", "green", "yellow"))
    }
    else if (input$Data == "Forward-UFA") {
      plot_ly(ForwardU, 
              x = ~CapHit, 
              y = ~TOI.G, color = ~Sh.G, size = ~Pts.G, 
              text = ~paste(First.Name,Last.Name, "(", Ctry, ")", "-", Team, Season), 
              colors = c("blue", "red" ,"orange", "green", "yellow"))
    }
    else if (input$Data == "Forward-RFA") {
      plot_ly(ForwardR, 
              x = ~CapHit, 
              y = ~TOI.G, color = ~Sh.G, size = ~Pts.G, 
              text = ~paste(First.Name,Last.Name, "(", Ctry, ")", "-", Team, Season), 
              colors = c("blue", "red" ,"orange", "green", "yellow"))
    }
    else if (input$Data == "Goalies-Rookie") {
      plot_ly(GoaliesN, 
              x = ~CapHit, 
              y = ~GS, color = ~SV., size = ~QS., 
              text = ~paste(First.Name,Last.Name, "(", Ctry, ")", "-", Team, Season), 
              colors = c("black" ,"blue", "red" , "green", "yellow"))
    }
    else if (input$Data == "Goalies-UFA") {
      plot_ly(GoaliesU, 
              x = ~CapHit, 
              y = ~GS, color = ~SV., size = ~QS., 
              text = ~paste(First.Name,Last.Name, "(", Ctry, ")", "-", Team, Season), 
              colors = c("black" ,"blue", "red" , "green", "yellow"))
    }
    else if (input$Data == "Goalies-RFA") {
      plot_ly(GoaliesR, 
              x = ~CapHit, 
              y = ~GS, color = ~SV., size = ~QS., 
              text = ~paste(First.Name,Last.Name, "(", Ctry, ")", "-", Team, Season), 
              colors = c("black" ,"blue", "red" , "green", "yellow"))
    }
  })
  
  output$Text = renderUI({
    #Text output in visualization
    if (input$Data == "Goalies-RFA" || input$Data == "Goalies-UFA" || input$Data == "Goalies-Rookie") {
      HTML(paste("Na grafe vidíme porovnanie platu brankárov (CapHit)",
      "V závislosti od počtu odohraných zápasov (GS)",
      "Veľkosť bodov je závislá od počtu kvalitných štartov brankára" ,
      "Farba bodov je závislá od úsešnosti zásahov", sep = "<br/>"))
    }
    else {
      HTML(paste("Na grafe vidíme porovnanie platu hráčov (CapHit)",
                 "V závislosti od priemerného počtu odohraných minút v zápase (TOI.G)",
                 "Veľkosť bodov je závislá od počtu bodov na zápas" ,
                 "Farba bodov je závislá od počtu striel na zápas", sep = "<br/>"))
    }
  })
  
  output$table = renderDataTable(
    #Table output in model
    if (input$Model == "Feature Selection") {
      (Feature)
    }
    else if (input$Model == "Stepwise Regression") {
      (Forward)
    }
    else if (input$Model == "Polynomial Regression") {
      (Poly)
    }, options = list(pageLength = 11))
  
  output$Text2 = renderUI({
    #Text output in model
    if (input$Model == "Feature Selection") {
      HTML(paste(strong("V tabuľke vidíme 10 najlepšie vyhodnotených atribútov podľa modelu Feature Selection pre tabuľky brankárov(G) a hráčov(P)."),
                 "Tieto atribúty sú usporiadané podľa relevantnosti.",
                 "V stĺpci G_Att nájdeme názvy atribútov u brankárov.",
                 "V Stĺpci G_Att_Value nájdeme hodnoty atribútov pri brankároch podľa tohto modelu.",
                 "V stĺpci P_Att nájdeme názvy atribútov u hráčov.",
                 "V Stĺpci P_Att_Value nájdeme hodnoty atribútov pri hráčoch podľa tohto modelu.",
                 sep = "<br/>"))
    }
    else if (input$Model == "Stepwise Regression") {
      HTML(paste(strong("V tabuľke vidíme výsledky modelu Stepwise Regression pre všetky tabuľky."),
                 "Tiež aj pre tabuľku všetkých hráčov a všetkých brankárov.",
                 "V stĺpci Precision nájdeme presnosť tohto modelu v %.",
                 "V Stĺpci Count nájdeme počet atribútov, ktoré tvoria najlepší model.",
                 "V stĺpci Best Combination nájdeme ideálnu kombináciu atribútov pri ktorých dosiahne model najvyššiu presnosť.",
                 sep = "<br/>"))
    }
    else if (input$Model == "Polynomial Regression") {
      HTML(paste(strong("V tabuľke vidíme výsledky modelu Polynomial Regression pre všetky tabuľky."),
                 "Tiež aj pre tabuľku všetkých hráčov a všetkých brankárov.",
                 "V stĺpci Precision nájdeme presnosť tohto modelu v %.",
                 "V stĺpci RMSE nájdeme priemernú odchýlku štvorcov.", sep = "<br/>"))
    }
  })

  output$model = renderPlot({
    #Button 'OK'
    #Graph output in Salary calculation
    input$OK
    isolate({
      if (input$Meno == ""){
        
      }
      else {
      barplot(c(CapHit[CapHit == input$Meno,2], CapHit[CapHit == input$Meno, 3]), col = c("blue", "green"), font.axis = 2, las = 1, yaxp = c(0,(round(max(c(CapHit[CapHit == input$Meno,2], CapHit[CapHit == input$Meno, 3])))+1),10))
      abline(h = CapHit[CapHit == input$Meno,2], lwd = 1, col = "black")
      abline(h = CapHit[CapHit == input$Meno,3], lwd = 1, col = "black")
      legend("topright", c(paste("Skutočný Plat: ",c(CapHit[CapHit == input$Meno,2], CapHit[CapHit == input$Meno, 3])[1],"M"), paste("Predikovaný Plat: ",c(CapHit[CapHit == input$Meno,2], CapHit[CapHit == input$Meno, 3])[2],"M")), fill = c("blue", "green"))
      }
      })
    })
}

shinyApp(ui = ui, server = server)
