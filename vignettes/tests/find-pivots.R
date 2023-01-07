spx <- quantmod::getSymbols("^GSPC", auto.assign = FALSE)
spx <- spx["2021-12-01::2023-01-01"]

sups <- techchart::find.pivots(spx, type = "FIB")
summary(sups)

# Ctrl-Shift-C: add block comments
# supports and resistance:
# next 3 supports:3585.62
# next 3 resistance:3873.278 4051.236 4195.065

srs <- techchart::find.pivots(spx, type = "SR", strength = 5)
summary(srs)

# supports and resistance:
# no supports at curret levels
# next 3 resistance:3911.106 4097.278 4184.266