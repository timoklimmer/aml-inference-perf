from locust import FastHttpUser, between, events, task


@events.init_command_line_parser.add_listener
def _(parser):
    parser.add_argument("--aml-webservice-auth-key", include_in_web_ui=True, default="")


class User(FastHttpUser):
    # specifiy a wait time as needed, when commented out/removed = no wait time
    #wait_time = between(0.05, 0.1)

    @task
    def test_api(self):
        self.client.post(
            "",
            # adjust the JSON here to fit your web service
            json={
                "dvcat": "1-9km/h",
                "seatbelt": "belted",
                "frontal": "frontal",
                "sex": "m",
                "ageOfocc": "16",
                "yearVeh": "2003",
                "airbag": "none",
                "occRole": "pass",
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.environment.parsed_options.aml_webservice_auth_key}",
            },
        )
