import app.io.input as app_in
import app.io.output as app_out

def main():
    data_from_console = app_in.from_console()
    app_out.to_console(data_from_console)
    app_out.to_file('./data/output.txt', data_from_console)

    data_from_file = app_in.from_file('./data/example.txt')
    app_out.to_console(data_from_file)
    app_out.to_file('./data/output.txt', data_from_file)

    data_from_file_pd = app_in.from_file_pd('./data/example.txt')
    app_out.to_console(data_from_file_pd)
    app_out.to_file('./data/output.txt', data_from_file_pd)


if __name__ == '__main__':
    main()
