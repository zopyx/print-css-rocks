import os
import subprocess
import commands


def run_ah(index_fn, pdf_fn, ah_options='ah.options', areatree=False):
    """ Run Antennahouse on given input file ``index.fn`` generating
        a PDF output file ``pdf_fn``.
    """

    dirname = os.path.dirname(index_fn)
    index_base, ext = os.path.splitext(os.path.basename(index_fn))

    if areatree:
        areatree_fn = os.path.join(dirname, '{}.parsetree'.format(index_base))
        cmd = 'run.sh -p @AreaTree -d "{}" | xmllint --format - >"{}"'.format(index_fn, areatree_fn)

    else:
        cmd = 'run.sh -d "{}" -o "{}"'.format(index_fn, pdf_fn)

    print cmd
    status, output = commands.getstatusoutput(cmd)
    if status != 0:
        raise RuntimeError('{} executed with status {}'.format(cmd, status))
    return output


if __name__ == '__main__':
    print run_ah('index.html', 'xx.pdf')

