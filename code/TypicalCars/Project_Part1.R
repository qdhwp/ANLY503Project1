##ANLY503 Project##

setwd("C:/Users/jacky/Desktop/HW/ANLY503/Project")
options(warn=-1)
rm(list=ls())
cat("\014")
dev.off()

#load libraries
library(MASS)
library(ggplot2)
library(dplyr)
library(reshape2)
library(GGally)

#load in data
mydata <- read.csv(file="cleaned_carscom.csv", header=TRUE, sep=",")
#mydata_1 <- read.csv(file="TrueCar_cleaned.csv", header=TRUE, sep=",")
mydata_1 <- read.csv(file="TrueCar_cleaned_Update.csv", header=TRUE, sep=",")

mydf <- data.frame(mydata)
mydf_1 <- data.frame(mydata_1)
mydata_2 <- read.table("class.txt", encoding="UTF-8")
mydf_2 <- data.frame(mydata_2)
colnames(mydf_2) <- c("Make", "Model", "New_Price")
mydf_2[, "Make"][1] <- "Mercedes-Benz"

#clean data and match brands/models
brands <- list(mydf_2['Make'])
models <- list(mydf_2['Model'])
condition <- mydf_1[, 'Make'] %in% c("Mercedes-Benz", "BMW", "Porsche", "Toyota", "Honda", "Nissan")
mybrands <- mydf_1[condition, , drop=FALSE]
condition_1 <- mybrands[, 'Model'] %in% c("S-ClassS350", "7", "Panamera4dr", "GL-ClassGL450", "X6xDrive35i", 
                                      "CayenneAWD", "CamryLE", "AccordLX", "Altima2.5", "RAV4LE", "CR-VLX", "RogueS")
mymodels <- mybrands[condition_1, , drop=FALSE]

#modify features
model_price <- merge(mymodels, mydf_2)
#model_price_clean <- model_price[, c("Make", "Model", "Price", "Year", "Mileage", "New_Price")]
model_price_clean <- model_price[, c("Make", "Model", "Price", "Year", "Mileage", "New_Price", "mile_per_year")]
model_price_clean[, "Year_Used"] <- 2018 - model_price_clean[, "Year"]
model_price_clean[, "Price_Difference"] <- model_price_clean[, "New_Price"] - model_price_clean[, "Price"]

##draw PCP
unique(model_price_clean["Model"])

model_price_clean["color"] <- "color"
#expensive cars
model_price_clean[1:1460, "color"] <- "blue"
model_price_clean[8050:8067, "color"] <- "blue"
model_price_clean[29650:29949, "color"] <- "blue"
#expensive SUVs
model_price_clean[1461:1676, "color"] <- "red"
model_price_clean[7120:8049, "color"] <- "red"
model_price_clean[28963:29649, "color"] <- "red"
#cheap cars
model_price_clean[29950:34979, "color"] <- "yellow"
model_price_clean[1677:3643, "color"] <- "yellow"
model_price_clean[8068:24891, "color"] <- "yellow"
#cheap SUVs
model_price_clean[34980:36511, "color"] <- "black"
model_price_clean[3644:7119, "color"] <- "black"
model_price_clean[24892:28962, "color"] <- "black"

parcoord(model_price_clean[, c(3:4, 7)], col=rainbow(length(model_price_clean[, 1])), lty=1:5, var.label=TRUE)
#parcoord(model_price_clean[, c(3:4, 6)], col=rainbow(length(model_price_clean[, 1])), lty=1:5, var.label=TRUE)
#parcoord(model_price_clean[, c(3:4, 6)], col=as.vector(model_price_clean["color"]), lty=1:5, var.label=TRUE)

#save the plot
dev.copy(png,'myplot_1.png')
dev.off()

#another way to draw PCP
model_grouped <- model_price_clean %>% group_by(model_price_clean[, "Model"], model_price_clean[, "Make"], 
                                                model_price_clean[, "Year"], model_price_clean[, "Mileage"], 
                                                model_price_clean[, "Price"]) %>% count()
model_grouped["id"] <- "id"
colnames(model_grouped) <- c("Model", "Make", "Year", "Mileage", "Price", "n", "id")
model_grouped <- data.frame(model_grouped)

for(i in 1:36430){
  model_grouped[i, "id"] = paste(model_grouped[i, "Make"], model_grouped[i, "Model"], 
                                 sep='-')
}

model_grouped <- (model_grouped %>% arrange(desc(n)))

##draw PCP
#ggparcoord(model_grouped, columns=3:5, groupColumn='id', scale='globalminmax')




##draw pictogram
dev.off()
library(ggplot2)
library(png)
library(jpeg)
library(grid)

#generate data
df3 <- data.frame(units = c(log(-(1-1460)), log(-(8050-8067)), log(-(29650-29949)), log(-(1461-1676)), 
                            log(-(7120-8049)), log(-(28963-29649)), log(-(29950-34979)), log(-(1677-3643)), 
                            log(-(8068-24891)), log(-(34980-36511)), log(-(3644-7119)), log(-(24892-28962))), 
                  what = c('7', 'S-ClassS350', 'Panamera4dr', 
                           'X6xDrive35i', 'GL-ClassGL450', 'CayenneAWD', 
                           'CamryLE', 'AccordLX', 'Altima2.5', 'RAV4LE', 'CR-VLX', 'RogueS'))
df3$what <- factor(df3$what, levels = df3$what, ordered = TRUE)

#define a helper function
fill_images <- function() {
  l <- list()
  for (i in 1:nrow(df3)) {
    for (j in 1:floor(df3$units[i])) {
      img <- readJPEG("0.jpg")
      #img <- readPNG(system.file("img", "Rlogo.png", package="png"))
      g <- rasterGrob(img, interpolate=TRUE)
      l <- c(l, annotation_custom(g, xmin = i-1/2, xmax = i+1/2, ymin = j-1, ymax = j))
    }
  }
  l
}

#plot
pic <- ggplot(df3, aes(what, units)) + 
  geom_bar(fill="white", colour="blue", alpha=0.1, stat="identity") + 
  coord_flip() + 
  scale_y_continuous(breaks=seq(0, 20, 2)) + 
  scale_x_discrete() + 
  theme_bw() + 
  theme(axis.title.x  = element_blank(), axis.title.y  = element_blank()) + 
  fill_images()
pic

#save the plot
dev.copy(png,'myplot_2.png')
dev.off()





##draw density plot
#dens <- density(model_price_clean$Price) # returns the density data 
#plot(dens) 

#par(mfrow=c(4,3))

#expensive cars
#dens_1 <- density(model_price_clean[1:1460, "Price"]) # returns the density data 
#plot(dens_1, main = "7") 

#dens_2 <- density(model_price_clean[8050:8067, "Price"]) # returns the density data 
#plot(dens_2, main = "S-ClassS350") 

#dens_3 <- density(model_price_clean[29650:29949, "Price"]) # returns the density data 
#plot(dens_3, main = "Panamera4dr") 

#expensive SUVs
#dens_4 <- density(model_price_clean[1461:1676, "Price"]) # returns the density data 
#plot(dens_4, main = "X6xDrive35i") 

#dens_5 <- density(model_price_clean[7120:8049, "Price"]) # returns the density data 
#plot(dens_5, main = "GL-ClassGL450") 

#dens_6 <- density(model_price_clean[28963:29649, "Price"]) # returns the density data 
#plot(dens_6, main = "CayenneAWD") 

#cheap cars
#dens_7 <- density(model_price_clean[29950:34979, "Price"]) # returns the density data 
#plot(dens_7, main = "CamryLE") 

#dens_8 <- density(model_price_clean[1677:3643, "Price"]) # returns the density data 
#plot(dens_8, main = "AccordLX") 

#dens_9 <- density(model_price_clean[8068:24891, "Price"]) # returns the density data 
#plot(dens_9, main = "Altima2.5") 

#cheap SUVs
#dens_10 <- density(model_price_clean[34980:36511, "Price"]) # returns the density data 
#plot(dens_10, main = "RAV4LE") 

#dens_11 <- density(model_price_clean[3644:7119, "Price"]) # returns the density data 
#plot(dens_11, main = "CR-VLX") 

#dens_12 <- density(model_price_clean[24892:28962, "Price"]) # returns the density data 
#plot(dens_12, main = "RogueS") 

#save the plot
#dev.copy(png,'myplot_3.png')
#dev.off()





##draw density plot
#dens <- density(model_price_clean$Price) # returns the density data 
#plot(dens) 

par(mfrow=c(4,3))

#expensive cars
dens_1 <- density(model_price_clean[1:1455, "Price"]) # returns the density data 
plot(dens_1, main = "7") 

dens_2 <- density(model_price_clean[7982:7999, "Price"]) # returns the density data 
plot(dens_2, main = "S-ClassS350") 

dens_3 <- density(model_price_clean[28843:29142, "Price"]) # returns the density data 
plot(dens_3, main = "Panamera4dr") 

#expensive SUVs
dens_4 <- density(model_price_clean[1456:1670, "Price"]) # returns the density data 
plot(dens_4, main = "X6xDrive35i") 

dens_5 <- density(model_price_clean[7055:7981, "Price"]) # returns the density data 
plot(dens_5, main = "GL-ClassGL450") 

dens_6 <- density(model_price_clean[28164:28842, "Price"]) # returns the density data 
plot(dens_6, main = "CayenneAWD") 

#cheap cars
dens_7 <- density(model_price_clean[29143:34087, "Price"]) # returns the density data 
plot(dens_7, main = "CamryLE") 

dens_8 <- density(model_price_clean[1671:3618, "Price"]) # returns the density data 
plot(dens_8, main = "AccordLX") 

dens_9 <- density(model_price_clean[8000:24235, "Price"]) # returns the density data 
plot(dens_9, main = "Altima2.5") 

#cheap SUVs
dens_10 <- density(model_price_clean[34088:35582, "Price"]) # returns the density data 
plot(dens_10, main = "RAV4LE") 

dens_11 <- density(model_price_clean[3619:7054, "Price"]) # returns the density data 
plot(dens_11, main = "CR-VLX") 

dens_12 <- density(model_price_clean[24236:28163, "Price"]) # returns the density data 
plot(dens_12, main = "RogueS") 

#save the plot
dev.copy(png,'myplot_4.png')
dev.off()




































