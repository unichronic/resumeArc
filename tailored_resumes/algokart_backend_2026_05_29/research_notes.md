# AlgoKart Research Notes

Source checked: https://algokart.trade/

AlgoKart appears to be a marketplace/platform for algorithmic trading strategies. The public app copy and bundled routes/features show:

- Marketplace for strategy discovery, unlocking, backtesting, and execution.
- Strategy creation flows for equity/basket/indicator strategies, including capital allocation, schedule, entry/exit conditions, and publishing.
- Wallet/credits flow used for unlocking strategies, running backtests, and execution.
- Broker connection and execution flows, including broker selection, secure authentication/OAuth-style copy, order review, and live/paper execution.
- Risk-control emphasis:
  - strategies without defined risk limits cannot be traded live;
  - strategy auto-stops after configured calendar duration;
  - partial fills are handled with risk controls only on filled quantity and unfilled quantity cancelled automatically;
  - each asset can execute independently with its own risk controls;
  - simulated backtests can differ from live results because of slippage, transaction costs, and execution quality.
- Internal/admin surface appears to include analyst/vendor/admin/audit flows.

Resume/mail positioning:

- Lead with backend/platform reliability, not frontend.
- Best fit projects: Penny Lane Capital for market research/backtesting/risk review; Postificus for queues/retries/DLQs/observability; Seaweed for concurrent backend platform work; Hyoka for trace/eval/replay/audit-control infrastructure.
- Bentham AI should be framed as recoverable automation around unreliable external systems, with `https://www.bentham.legal/` included whenever mentioned in mail.
