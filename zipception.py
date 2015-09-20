import io
import sys
import zipfile


def main():
    try:
        filename = sys.argv[1]
        iterations = abs(int(sys.argv[2]))
    except:
        print 'usage:  %s file iterations' % sys.argv[0]
        sys.exit(1)

    with open(filename, 'rb') as f:
        data = f.read()

    for _ in xrange(iterations - 1):
        output = io.BytesIO()
        zipf = zipfile.ZipFile(output, mode='w')
        zipf.writestr(filename, data)
        zipf.close()
        output.seek(0)
        data = output.read()
        filename = filename + '.zip'

    zipf = zipfile.ZipFile(filename + '.zip', mode='w')
    zipf.writestr(filename, data)
    zipf.close()

if __name__ == '__main__':
    main()
