from func.src.domain.validator import Onboarding


class OnboardingSnapshotRepository:
    @staticmethod
    def snapshot(onboarding: Onboarding) -> list:
        onboarding_fields = [{
            "Campo": "Faltou fazer",
            "BR": onboarding.missing_step_br,
            "US": onboarding.missing_step_us,
        }, {
            "Campo": "Data da Ultima",
            "BR": "??/??/????",
            "US": "??/??/????",
        }]
        return onboarding_fields
