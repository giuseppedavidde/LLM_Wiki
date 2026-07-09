---
title: "Options Strategies"
type: concept
tags: [options, greeks, volatility, crypto, scalping, contrarian, sentiment]
sources: ["[[sources/volume-profile]]", "[[sources/options-trading-crash-course]]", "[[sources/the-options-playbook]]", "[[sources/the-options-course-workbook]]"]
last_updated: 2026-07-09
---

> Sources: Brian Overby, The Options Playbook; George Fontanills, The Options Course Workbook; Unknown Author, Options Crash Course
> Raw: [Options Playbook](../../raw/options/the-options-playbook-expanded-2nd-edition-featuring-40-strategies-for-bulls-bear.md); [Options Course Workbook](../../raw/options/the-options-course-workbook-step-by-step-exercises-and-tests-to-help-you-master-.md); [Options Crash Course](../../raw/options/options-trading-crash-course-advanced-guide-to-make-money-with-options-trading-i.md)

## Overview

Options strategies span from simple single-leg directional bets to multi-leg volatility trades combining four or more contracts. This reference covers all major strategies organized by complexity, market outlook, and risk profile. Each entry includes the setup, breakeven, max profit/loss, volatility bias, and time decay bias as described by Overby, Fontanills, and the Crash Course authors.

Greeks notation: Δ (delta), Γ (gamma), Θ (theta), ν (vega).

---

## 1. Single-Leg Strategies

### Long Call

- **Setup**: Buy a call, strike A. Stock at or above strike A.
- **Outlook**: Bullish.
- **Max Profit**: Unlimited (stock rises infinitely).
- **Max Loss**: Premium paid for the call.
- **Breakeven**: Strike A + premium paid.
- **Volatility Bias**: Want IV to increase (raises call value).
- **Time Decay**: Enemy — Θ erodes the option value.
- **Greeks**: Δ positive (0 to 1), Γ positive (highest ATM near expiration), Θ negative, ν positive.

The long call gives the right to buy stock at strike A. It offers leverage over buying stock outright with limited downside (Fontanills: "risk is the price of the premium"). Overby warns against buying too many OTM short-term calls — timing must be right and the stock must exceed strike plus cost just to break even.

### Long Put

- **Setup**: Buy a put, strike A. Stock at or below strike A.
- **Outlook**: Bearish.
- **Max Profit**: Strike A − premium paid (if stock goes to zero).
- **Max Loss**: Premium paid.
- **Breakeven**: Strike A − premium paid.
- **Volatility Bias**: Want IV to increase.
- **Time Decay**: Enemy.
- **Greeks**: Δ negative (−1 to 0), Γ positive, Θ negative, ν positive.

An alternative to short stock without unlimited upside risk. Can also serve as a hedge on a long stock position (protective put).

### Short Call (Naked Call)

- **Setup**: Sell a call, strike A. Stock below strike A.
- **Outlook**: Bearish to neutral.
- **Max Profit**: Premium received.
- **Max Loss**: Theoretically unlimited (stock rises infinitely).
- **Breakeven**: Strike A + premium received.
- **Volatility Bias**: Want IV to decrease.
- **Time Decay**: Friend — Θ erodes the short option value.
- **Greeks**: Δ negative, Γ negative, Θ positive, ν negative.

Overby reserves this for All-Stars only. The sweet spot is large — as long as stock stays below strike A at expiration, full premium is kept. Selling options ~1 standard deviation OTM increases probability of success.

### Short Put (Naked Put)

- **Setup**: Sell a put, strike A. Stock above strike A.
- **Outlook**: Bullish to neutral.
- **Max Profit**: Premium received.
- **Max Loss**: Strike A − premium received (if stock goes to zero).
- **Breakeven**: Strike A − premium received.
- **Volatility Bias**: Want IV to decrease.
- **Time Decay**: Friend.
- **Greeks**: Δ positive, Γ negative, Θ positive, ν negative.

Fontanills notes risk is "limited to the stock falling to zero" — substantial but not unlimited like short calls. Overby recommends using index options for reduced volatility risk.

---

## 2. Income / Covered Strategies

![Covered call payoff diagram](images/playbook_p58_2.jpeg)

### Covered Call (Buy-Write)

- **Setup**: Own 100 shares stock + sell 1 call, strike A. Stock below strike A.
- **Outlook**: Neutral to mildly bullish. Willing to sell stock at strike A.
- **Max Profit**: (Strike A − current stock price) + premium received.
- **Max Loss**: Stock can lose value (minus premium cushion).
- **Breakeven**: Stock purchase price − premium received.
- **Volatility Bias**: Want IV to decrease.
- **Time Decay**: Friend.
- **Greeks**: Overall Δ positive (stock Δ = 1, call Δ reduces it), Θ positive.

The classic beginner strategy (Play A in Overby's Rookies' Corner). The call sold generates income; the stock covers assignment risk. Overby suggests 30–45 days to expiration targeting ~2% of stock value as premium. Fontanills describes it as a strategy where "the shares are held and a call is written against the position." The upside is capped; the downside is the stock's decline partially offset by the call premium.

### Cash-Secured Put

- **Setup**: Sell a put, strike A + hold enough cash to buy stock if assigned.
- **Outlook**: Slightly bearish short-term; bullish long-term (want to acquire stock cheaper).
- **Max Profit**: Premium received (or long stock gains if assigned).
- **Max Loss**: Strike A − premium received (if stock goes to zero).
- **Breakeven**: Strike A − premium received.
- **Volatility Bias**: Want IV to decrease.
- **Time Decay**: Friend.

A substitute for a limit order to buy stock. If the stock dips below strike A, you're assigned and acquire the stock at a net lower cost (strike minus premium). If it stays above, you keep the premium. Overby recommends 30–45 DTE, selling slightly OTM. "It's one of the few instances where you can profit by being wrong."

### Protective Put (Married Put)

- **Setup**: Own stock + buy a put, strike A.
- **Outlook**: Bullish but nervous — downside protection.
- **Max Profit**: Unlimited (uncapped stock upside).
- **Max Loss**: (Stock price − strike A) + premium paid (the "deductible").
- **Breakeven**: Stock price + premium paid.
- **Volatility Bias**: Want IV to increase.
- **Time Decay**: Enemy.
- **Greeks**: Overall Δ positive (reduced by put Δ), Θ negative.

Acts as insurance on a long stock position. Overby notes it is an alternative to a stop order, with the advantage that the put guarantees a floor price (unlike stops which can gap). When established simultaneously with stock purchase, it is called a *married put*. Fontanills calls it a "stock insurance policy."

### Collar

- **Setup**: Own stock + buy put (strike A) + sell call (strike B). Stock between A and B.
- **Outlook**: Bullish but cautious — protect gains.
- **Max Profit**: Strike B − stock price − net debit (+ net credit).
- **Max Loss**: Stock price − strike A + net debit (− net credit).
- **Breakeven**: Stock price − net credit (credit collar) or + net debit (debit collar).
- **Volatility Bias**: Neutral — IV affects both legs.
- **Time Decay**: Neutral — short leg benefits, long leg hurts.

Simultaneously runs a protective put (floor) and a covered call (cap). The call premium can partially or fully offset the put cost — a *zero-cost collar* when strikes are chosen so the premium received equals the premium paid. Fontanills and Overby both present this as a risk management tool for appreciated stock positions.

### Fig Leaf (LEAPS Diagonal / Leveraged Covered Call)

- **Setup**: Buy ITM LEAPS call (strike A) + sell OTM short-term call (strike B).
- **Outlook**: Mildly bullish.
- **Max Profit**: Limited — depends on LEAPS performance and premiums from rolling short calls.
- **Max Loss**: Net debit paid.
- **Volatility Bias**: Somewhat neutral.
- **Time Decay**: Friend — front-month short call decays faster than LEAPS long call.

A covered call substitute using a LEAPS call instead of stock. Requires less capital than buying 100 shares. Overby recommends a delta of .80 or more on the LEAPS call (at least 20% ITM). The short call is rolled monthly; assignment must be avoided since you don't own the stock.

---

## 3. Vertical Spreads (Single-Expiration, Different Strikes)

All vertical spreads share the same expiration month for both legs. They are defined by the position's net debit (paid) or net credit (received).

### Bull Call Spread (Long Call Spread)

- **Setup**: Buy call (strike A) + sell call (strike B, higher). Same expiration.
- **Outlook**: Bullish with upside target.
- **Max Profit**: (Strike B − strike A) − net debit paid.
- **Max Loss**: Net debit paid.
- **Breakeven**: Strike A + net debit paid.
- **Volatility Bias**: Mixed — depends on stock position relative to strikes.
- **Time Decay**: Neutral — erodes both legs.
- **Greeks**: Δ positive but < long call alone, Γ positive, Θ near-neutral, ν small.

An alternative to a plain long call — the short call at strike B offsets cost but caps upside. Fontanills: "the bull call spread reduces the cost of a straight call purchase while limiting profit potential." Overby recommends 30–45 DTE.

### Bear Put Spread (Long Put Spread)

- **Setup**: Sell put (strike A) + buy put (strike B, higher). Same expiration.
- **Outlook**: Bearish with downside target.
- **Max Profit**: (Strike B − strike A) − net debit paid.
- **Max Loss**: Net debit paid.
- **Breakeven**: Strike B − net debit paid.
- **Volatility Bias**: Mixed.
- **Time Decay**: Neutral.
- **Greeks**: Δ negative, Γ positive, Θ near-neutral, ν small.

Play 11 in Overby's book (AKA Bear Put Spread). Offsets cost of a long put by selling a cheaper lower-strike put. Fontanills recommends this when IV is high to neutralize volatility effects.

### Bear Call Spread (Short Call Spread)

- **Setup**: Sell call (strike A) + buy call (strike B, higher). Same expiration.
- **Outlook**: Bearish to neutral.
- **Max Profit**: Net credit received.
- **Max Loss**: (Strike B − strike A) − net credit received.
- **Breakeven**: Strike A + net credit received.
- **Volatility Bias**: Want IV to decrease if stock is near strikes.
- **Time Decay**: Somewhat positive.
- **Greeks**: Δ negative, Γ negative, Θ positive, ν negative.

A credit strategy — you receive money upfront. Overby suggests selling ~1 standard deviation OTM. Both options ideally expire worthless. Fontanills warns: "the risk is limited but still significant."

### Bull Put Spread (Short Put Spread)

- **Setup**: Buy put (strike A) + sell put (strike B, higher). Same expiration.
- **Outlook**: Bullish to neutral.
- **Max Profit**: Net credit received.
- **Max Loss**: (Strike B − strike A) − net credit received.
- **Breakeven**: Strike B − net credit received.
- **Volatility Bias**: Want IV to decrease.
- **Time Decay**: Somewhat positive.
- **Greeks**: Δ positive, Γ negative, Θ positive, ν negative.

The bullish credit spread counterpart to the bear call. Maximum profit when stock is above strike B at expiration. Overby: "you want both options to expire worthless."

---

## 4. Multi-Leg Volatility Strategies

![Straddle and strangle payoff diagrams](images/playbook_p74_1.jpeg)

### Long Straddle

- **Setup**: Buy ATM call (strike A) + buy ATM put (strike A). Same expiration.
- **Outlook**: Expect large move in either direction (long volatility).
- **Max Profit**: Unlimited upside; substantial but limited downside (to strike A − net debit).
- **Max Loss**: Net debit paid (both premiums).
- **Breakevens**: Strike A + net debit (upside); Strike A − net debit (downside).
- **Volatility Bias**: Want IV to increase — doubly beneficial.
- **Time Decay**: Mortal enemy — Θ works against both legs.
- **Greeks**: Δ near 0 initially (delta neutral), Γ positive, Θ strongly negative, ν strongly positive.

The purest volatility play. Fontanills: "a long straddle makes money when the underlying asset moves sharply in either direction... the call increases faster than the put loses money, and vice versa." Optimal entry is when IV is low expecting a volatility increase (e.g., ahead of earnings). Overby warns the stock must move significantly just to break even.

### Short Straddle

- **Setup**: Sell ATM call (strike A) + sell ATM put (strike A). Same expiration.
- **Outlook**: Neutral — expect minimal movement (short volatility).
- **Max Profit**: Net credit received.
- **Max Loss**: Unlimited upside; substantial downside (strike A − net credit).
- **Breakevens**: Strike A + net credit (upside); Strike A − net credit (downside).
- **Volatility Bias**: Want IV to decrease — doubly beneficial.
- **Time Decay**: Best friend — Θ works for both legs.
- **Greeks**: Δ near 0, Γ negative, Θ positive, ν strongly negative.

Fontanills does not recommend placing unlimited risk strategies but includes them for completeness. Overby reserves this for All-Stars only. Best when IV is high expecting a volatility crush.

### Long Strangle

- **Setup**: Buy OTM put (strike A) + buy OTM call (strike B, higher). Same expiration.
- **Outlook**: Expect very large move in either direction.
- **Max Profit**: Unlimited upside; limited downside (strike A − net debit).
- **Max Loss**: Net debit paid.
- **Breakevens**: Strike A − net debit (downside); Strike B + net debit (upside).
- **Volatility Bias**: Want IV to increase.
- **Time Decay**: Mortal enemy.
- **Greeks**: Δ near 0, Γ positive, Θ negative, ν positive.

Cheaper than a straddle because both legs are OTM. However, the stock must move even more to profit. Overby: "a straddle costs more but the stock doesn't have to move as far." Fontanills: "the maximum loss area is wider... the underlying has to see a larger move."

### Short Strangle

- **Setup**: Sell OTM put (strike A) + sell OTM call (strike B). Same expiration.
- **Outlook**: Neutral — expect stock to stay within range.
- **Max Profit**: Net credit received.
- **Max Loss**: Unlimited upside; substantial downside (strike A − net credit).
- **Breakevens**: Strike A − net credit (downside); Strike B + net credit (upside).
- **Volatility Bias**: Want IV to decrease.
- **Time Decay**: Best friend.
- **Greeks**: Δ near 0, Γ negative, Θ positive, ν negative.

Overby suggests strikes ~1 standard deviation OTM. Wider sweet spot than short straddle but lower premium. High probability of profit if stock stays range-bound.

![Iron condor structure](images/playbook_p78_1.jpeg)

### Iron Condor

- **Setup**: Buy put (A) + sell put (B) + sell call (C) + buy call (D). A < B < C < D. Stock between B and C.
- **Outlook**: Neutral — expect range-bound movement.
- **Max Profit**: Net credit received.
- **Max Loss**: (B − A) − net credit (or C − D, symmetric).
- **Breakevens**: B − net credit (downside); C + net credit (upside).
- **Volatility Bias**: Want IV to decrease.
- **Time Decay**: Friend.
- **Greeks**: Δ near 0, Γ slightly negative, Θ positive, ν negative.

A short put spread below the market combined with a short call spread above. Overby considers this more attractive than a long condor because you receive a credit upfront. Fontanills recommends using index options for lower volatility risk. The Crash Course notes: "the iron condor should only be used if trading via index options as they offer decreased volatility and risk."

### Iron Butterfly

- **Setup**: Sell ATM straddle + buy OTM put and OTM call (wings). All same expiration.
- **Outlook**: Neutral — stock expected to stay at center strike at expiration.
- **Max Profit**: Net credit received.
- **Max Loss**: Wing width − net credit.
- **Breakevens**: Center strike ± net credit.
- **Volatility Bias**: Want IV to decrease.
- **Time Decay**: Friend.
- **Greeks**: Δ near 0, Γ slightly negative, Θ positive, ν negative.

Similar to iron condor but the short strikes are at the same ATM price. Narrower sweet spot, higher credit. The Crash Course describes it as utilizing "a mixture of puts and calls to limit the potential for loss (but also profits) around the strike price."

---

![Calendar spread example](images/playbook_p189_1.jpeg)

## 5. Calendar / Diagonal Spreads (Different Expirations)

### Calendar Call Spread

- **Setup**: Buy back-month call (strike A) + sell front-month call (strike A, same strike).
- **Outlook**: Neutral to slightly bullish — expect stock near strike A at front expiration.
- **Max Profit**: Achieved when stock is at strike A at front expiration.
- **Max Loss**: Net debit paid.
- **Volatility Bias**: Mixed — benefits from IV increase in back month, decrease in front month.
- **Time Decay**: Friend — front-month decays faster.
- **Greeks**: Theta positive overall (net short front-month time), Vega mixed.

Takes advantage of the accelerated time decay of the front-month option. Overby's Play 24 (Long Calendar Spread w/ Calls). The back-month long call retains value as the front-month short call decays.

### Calendar Put Spread

- **Setup**: Buy back-month put (strike A) + sell front-month put (strike A).
- **Outlook**: Neutral to slightly bearish.
- **Max Profit**: Stock at strike A at front expiration.
- **Max Loss**: Net debit.
- **Volatility Bias**: Mixed.
- **Time Decay**: Friend.

Overby's Play 25. Same mechanics as calendar call spread but using puts.

### Diagonal Spread

- **Setup**: Long back-month option (strike A) + short front-month option (strike B). Different strikes AND different expirations.
- **Outlook**: Varies — bullish with call diagonal, bearish with put diagonal.
- **Max Profit**: Limited — approximated via pricing model.
- **Max Loss**: Net debit paid.
- **Volatility Bias**: Somewhat neutral.
- **Time Decay**: Friend — front-month decays faster.

Combines calendar and vertical spread characteristics. Overby's Plays 26–27. The diagonal is the building block for the Fig Leaf and Double Diagonal. Exact breakeven is hard to calculate because of two expiration dates.

### Double Diagonal

- **Setup**: Buy OTM back-month put (A) + buy OTM back-month call (D) + sell front-month put (B) + sell front-month call (C). A < B < stock < C < D.
- **Outlook**: Neutral — expect minimal movement over multiple cycles.
- **Max Profit**: Approximated — net credits from rolling short options minus back-month debit.
- **Max Loss**: Limited to (B − A) minus credits.
- **Volatility Bias**: Want volatility to increase around front expiration (to boost roll credit), then decrease.
- **Time Decay**: Friend.
- **Greeks**: Complex — multi-leg, multi-expiration.

Overby's Play 40, the most complex in the book. Combines a put diagonal and a call diagonal. At front-month expiration, the short options are rolled to match the back-month expiration, converting the position into an iron condor. You capture premium twice.

---

## 6. Advanced Strategies

### Ratio Spreads (Front Spread / 1×2)

- **Setup**: Buy 1 option (strike A) + sell 2 options (strike B). Same expiration.
- **Outlook**: Slightly bullish (calls) or slightly bearish (puts) — want price at strike B at expiration.
- **Max Profit**: Difference between strikes ± net credit/debit.
- **Max Loss**: Unlimited (call front spread upside); substantial (put front spread downside).
- **Volatility Bias**: Want IV to decrease.
- **Time Decay**: Friend.
- **Greeks**: Complex — net short vega and gamma.

Overby's Plays 20–21 (AKA Ratio Vertical Spread). One of the sold options is uncovered, creating significant risk. Establishment for a net credit is ideal. Overby recommends using index options to reduce volatility risk.

### Backspreads (1×2+)

- **Setup**: Sell 1 option (strike A) + buy 2 options (strike B). Same expiration.
- **Outlook**: Extremely bullish (call backspread) or extremely bearish (put backspread) on a volatile stock.
- **Max Profit**: Unlimited upside (call backspread).
- **Max Loss**: (B − A) minus net credit (or plus net debit).
- **Volatility Bias**: Want IV to increase.
- **Time Decay**: Depends — enemy if stock near strike B, friend if below.
- **Greeks**: Net long gamma and vega.

Overby's Plays 22–23 (AKA Ratio Volatility Spread / Pay Later Call/Put). Ideal ahead of major news events. The risk graph looks ugly at expiration if stock only makes a small move, but the trade can profit earlier if volatility spikes.

### Box Spread

- **Setup**: Bull call spread + bear put spread at same strikes (buy call A + sell call B + buy put B + sell put A). Same expiration.
- **Outlook**: Arbitrage — theoretically risk-free (difference between spread cost and intrinsic value).
- **Max Profit**: Strike width minus net debit.
- **Max Loss**: Limited.
- **Volatility Bias**: Neutral.
- **Time Decay**: None (all same expiration).

A pure arbitrage strategy exploiting mispricing between call and put parity. Rarely profitable for retail traders due to transaction costs and competition from professional arbitrageurs. Not explicitly covered in the three source books but is a recognized advanced strategy.

![Butterfly spread risk graph](images/playbook_p209_1.jpeg)

### Butterflies & Condors (Long)

- **Setup**: Long butterfly = buy lower strike + sell 2 middle strikes + buy higher strike. Long condor = buy A + sell B + sell C + buy D (non-overlapping short strikes).
- **Outlook**: Neutral — stock expected at center strikes.
- **Max Profit**: Achieved at middle strike(s).
- **Max Loss**: Net debit paid.
- **Volatility Bias**: Want IV to decrease.
- **Time Decay**: Friend.
- **Greeks**: Short gamma and vega overall.

Overby covers extensive butterfly variations: long butterfly w/ calls (Play 28), long butterfly w/ puts (Play 29), skip strike butterfly (Plays 31–32), inverse skip strike butterfly (Plays 33–34), and Christmas tree butterfly (Plays 35–36). Also long condor spreads w/ calls/puts (Plays 37–38). The Crash Course describes the butterfly as "a combination of a bear spread and a traditional bull strategy which uses a total of three strike points."

### Ladders / Christmas Tree

- **Setup**: Three strikes — typically buy 1 lower strike, sell 1 middle strike, sell 1 higher strike (call ladder).
- **Outlook**: Directionally biased with defined risk and a "gap" area of max profit.
- **Max Profit**: Limited — defined by strike widths.
- **Max Loss**: Limited.
- **Volatility Bias**: Neutral to short volatility.

Overby's Christmas Tree Butterfly (Plays 35–36). Named for the stepped risk profile resembling a Christmas tree. Similar to a butterfly but with uneven strike spacing.

### Synthetic Positions

#### Synthetic Long Stock

- **Setup**: Buy call (strike A) + sell put (strike A). Same expiration.
- **Outlook**: Bullish.
- **Max Profit**: Unlimited.
- **Max Loss**: Strike A + net debit (− net credit).
- **Breakeven**: Strike A + net debit (− net credit).
- **Greeks**: Δ ≈ +1, Θ near-neutral, ν near-neutral.

Overby's Play 18 (AKA Long Combination / Combo). Risk/reward profile nearly identical to owning 100 shares, but with leverage — you achieve the same exposure without the full capital outlay. Established for a small net debit or credit depending on where stock is relative to strike.

#### Synthetic Short Stock

- **Setup**: Sell call (strike A) + buy put (strike A). Same expiration.
- **Outlook**: Bearish.
- **Max Profit**: Strike A + net credit (− net debit) if stock goes to zero.
- **Max Loss**: Unlimited.
- **Breakeven**: Strike A + net credit (− net debit).
- **Greeks**: Δ ≈ −1, Θ near-neutral, ν near-neutral.

Overby's Play 19 (AKA Short Combination / Combo). Mirrors short stock risk/reward. Used to avoid margin tied up in short stock position. Dividends are not owed (unlike actual short stock).

### Box Spread (Recap)

See note above — a synthetic risk-free position created by combining synthetic long stock and synthetic short stock at different strikes (or a bull call + bear put spread at same strikes). The payoff is a fixed amount at expiration, and the trade profits if the market price differs from theoretical value.

---

## 7. Strategy Selection Framework

### By Market Outlook

| Outlook | Strategies |
|---------|-----------|
| Strongly bullish | Long call, long call spread, synthetic long stock, call backspread |
| Mildly bullish | Covered call, bull put spread, fig leaf |
| Strongly bearish | Long put, bear put spread, synthetic short stock, put backspread |
| Mildly bearish | Bear call spread |
| Neutral / range-bound | Short straddle, short strangle, iron condor, iron butterfly, calendar spreads |
| Volatile (big move, unknown direction) | Long straddle, long strangle |

### By Volatility Environment

**High implied volatility → Sell premium (credit strategies):**
- Short straddle / strangle
- Iron condor / iron butterfly
- Bear call spread / bull put spread
- Covered call

**Low implied volatility → Buy premium (debit strategies):**
- Long straddle / strangle
- Long call / long put
- Vertical debit spreads (bull call, bear put)

Fontanills: "To place a long straddle, it is optimal to locate a market with low volatility expecting a volatility increase." Overby: "If implied volatility is abnormally high for no apparent reason, the call and put may be overvalued" — attractive for sellers.

### By Time Horizon

- **0–30 DTE (short-term):** High gamma risk, rapid theta decay. Favor credit spreads, short strangles, covered calls, weekly options.
- **30–90 DTE (medium-term):** Sweet spot for most strategies. Overby recommends 30–45 DTE for covered calls, vertical spreads, and iron condors.
- **90+ DTE (long-term / LEAPS):** Theta decay is slower, vega is higher. Favor long calls/puts, calendar spreads, fig leaf, synthetic positions.

### Risk/Reward Profiles

| Profile | Strategies |
|---------|-----------|
| Unlimited profit, limited risk | Long call, long put, long straddle, long strangle, synthetic long stock |
| Limited profit, unlimited risk | Short call (naked), short straddle |
| Limited profit, limited risk | All vertical spreads, iron condor, iron butterfly, butterfly, box spread |
| Unlimited profit, unlimited risk | Short stock (not an option strategy per se — but included via synthetic) |

### Greeks Summary by Strategy

| Strategy | Delta | Gamma | Theta | Vega |
|----------|-------|-------|-------|------|
| Long Call | + | + | − | + |
| Long Put | − | + | − | + |
| Short Call | − | − | + | − |
| Short Put | + | − | + | − |
| Covered Call | + (reduced) | − | + | − |
| Protective Put | + (reduced) | + | − | + |
| Bull Call Spread | + (moderate) | + | ~0 | ~0 |
| Bear Put Spread | − (moderate) | + | ~0 | ~0 |
| Bear Call Spread | − | − | + | − |
| Bull Put Spread | + | − | + | − |
| Long Straddle | ~0 | + | − − | + + |
| Short Straddle | ~0 | − | + + | − − |
| Long Strangle | ~0 | + | − | + |
| Short Strangle | ~0 | − | + | − |
| Iron Condor | ~0 | − | + | − |
| Iron Butterfly | ~0 | − | + | − |
| Calendar Call | ~0 | − (front) | + | ~0 |
| Ratio Spread (1×2) | ~0 | − | + | − |
| Backspread (1×2) | ~0 | + | varies | + |

Note: Greeks are approximate at initiation. They change dynamically as the underlying moves and time passes (gamma accelerates change in delta, especially near expiration).

---

## See Also

- [[options-fundamentals|Options Fundamentals]]
- [[options-greeks|Options Greeks]]
- [[options-volatility|Options Volatility]]
- [[contrarian-sentiment-analysis|Contrarian Sentiment Analysis]]
## 🔗 Graph Connections

| Concept | Relation | Source |
|---|---|---|
| Bear Put Spread | Defines | EXTRACTED |
| Bull Call Spread | Defines | EXTRACTED |
| Buy Write | Conceptually Related To | EXTRACTED |
| Call Option | Strategy For | EXTRACTED |
| Collar | Defines | EXTRACTED |
| Covered Call | Defines | EXTRACTED |
| Fig Leaf | Conceptually Related To | EXTRACTED |
| LEAPS (Long-Term Equity Options) | Strategy For | EXTRACTED |
| Protective Put | Defines | EXTRACTED |
| Put Option | Strategy For | EXTRACTED |
| Vertical Spread | Defines | EXTRACTED |
