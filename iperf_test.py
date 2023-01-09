import parser

class TestSuite():

    def test_iperf3_client_connection(self, server, client):
        stdout, error = client
        print(f'stdout received from fixture client:\n{stdout}')

        assert not error

        parsed_stdout = parser.parse(stdout)
        assert parsed_stdout['Transfer'] > 20 and parsed_stdout['Bandwidth'] > 20


    def test_iperf3_client_connection(self, server, client):
        stdout, error = client
        print(f'stdout received from fixture client:\n{stdout}')

        assert not error

        parsed_stdout = parser.parse(stdout)
    assert parsed_stdout['Transfer'] > 1 and parsed_stdout['Bandwidth'] > 1
