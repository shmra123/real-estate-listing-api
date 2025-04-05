from real_estate_listing_api.states.app_state import AppState


def get_state() -> AppState:
    """Get the app state

    Returns:
        AppState: The AppState instance
    """
    if AppState._instance is None:
        AppState._instance = AppState()
    return AppState._instance
