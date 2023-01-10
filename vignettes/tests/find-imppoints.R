# install_github("wgong/techchart")
getwd()
setwd("~/projects/wgong/techchart/vignettes/tests")

library(quantmod)
library(techchart)

symbol = "^GSPC"
symbol = "SPY"
spx_all <- getSymbols(symbol, auto.assign = FALSE)
# dim(spx_all)
View(spx_all)
# missing today's quote

# spx <- spx_all["2022::2023"]
spx <- spx_all["2021-12-01::2022-10-15"]


## find pivot points
imppts <- techchart::find.imppoints(spx,2)
x <- print(imppts)
write.csv(x, file="~/projects/wgong/techchart/vignettes/tests/imppoints-spy.csv")

chart_Series(spx)
# R plot symbols:
# http://www.sthda.com/english/wiki/r-plot-pch-symbols-the-different-point-shapes-available-in-r
points(as.numeric(imppts$maxima$pos), as.numeric(imppts$maxima$value), bg="red",pch=25,  cex=1.25)
points(as.numeric(imppts$minima$pos), as.numeric(imppts$minima$value), bg="green",pch=24,  cex=1.25)

## find trends
cpts = techchart::find.major.trends(spx)
summary(cpts)

quantmod::chart_Series(spx)
quantmod::add_TA(cpts$segments[[1]],on=1,lty=3, col="red")
quantmod::add_TA(cpts$segments[[2]],on=1,lty=3, col="red")

## find support/resistance
levels_fib = techchart::find.pivots(spx, type = "FIB")
levels_sr = techchart::find.pivots(spx, type = "SR", strength =3)

summary(levels_fib)
summary(levels_sr)
