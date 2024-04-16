import sentry_sdk # type: ignore

sentry_sdk.init(
    dsn="https://72055f9498bdbd2a282a4f542fc211ab@o4507092510113792.ingest.us.sentry.io/4507092511358976",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

division_by_zero = 1 / 0