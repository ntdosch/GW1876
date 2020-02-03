"""
mfswr module.  Contains the ModflowSwr1 class. Note that the user can access
the ModflowSwr1 class as `flopy.modflow.ModflowSwr1`.

Additional information for this MODFLOW process can be found at the `Online
MODFLOW Guide
<http://water.usgs.gov/ogw/modflow-nwt/MODFLOW-NWT-Guide/swr.htm>`_.

"""
import sys
from ..pakbase import Package


class ModflowSwr1(Package):
    """
    MODFLOW Surface-Water Routing Class.

    Parameters
    ----------
    model : model object
        The model object (of type :class:`flopy.modflow.mf.Modflow`) to which
        this package will be added.
    extension : string
        Filename extension (default is 'swr')
    unitnumber : int
        File unit number (default is None).
    filenames : str or list of str
        Filenames to use for the package. If filenames=None the package name
        will be created using the model name and package extension. If a
        single string is passed the package will be set to the string.
        Default is None.


    Attributes
    ----------

    Methods
    -------


    See Also
    --------

    Notes
    -----
    SWR1 Class is only used to write SWR1 filename to name file. Full
    functionality still needs to be implemented.

    Examples
    --------

    >>> import flopy
    >>> m = flopy.modflow.Modflow()
    >>> swr = flopy.modflow.ModflowSwr1(m)

    """

    def __init__(self, model, extension='swr', unitnumber=None,
                 filenames=None):
        """
        Package constructor.

        """
        # set default unit number of one is not specified
        if unitnumber is None:
            unitnumber = ModflowSwr1.defaultunit()

        # set filenames
        if filenames is None:
            filenames = [None]
        elif isinstance(filenames, str):
            filenames = [filenames]

        # Fill namefile items
        name = [ModflowSwr1.ftype()]
        units = [unitnumber]
        extra = ['']

        # set package name
        fname = [filenames[0]]

        # Call ancestor's init to set self.parent, extension, name and
        # unit number
        Package.__init__(self, model, extension=extension, name=name,
                         unit_number=units, extra=extra, filenames=fname)

        # check if a valid model version has been specified
        if model.version == 'mf2k' or model.version == 'mfusg':
            err = 'Error: cannot use {} package with model version {}'.format(
                self.name, model.version)
            raise Exception(err)

        self.heading = '# {} package for '.format(self.name[0]) + \
                       ' {}, '.format(model.version_types[model.version]) + \
                       'generated by Flopy.'
        self.url = 'swr1.htm'

        self.parent.add_package(self)

    def write_file(self):
        """
        Write the package file.

        Returns
        -------
        None

        """
        print('SWR1 write method not implemented yet')
        # f = open(self.fn_path, 'w')
        # f.write('{0}\n'.format(self.heading))
        # f.close()

    @staticmethod
    def load(f, model, ext_unit_dict=None):
        """
        Load an existing package.

        Parameters
        ----------
        f : filename or file handle
            File to load.
        model : model object
            The model object (of type: class:`flopy.modflow.mf.Modflow`)
            to which this package will be added.
        ext_unit_dict : dictionary, optional
            If the arrays in the file are specified using EXTERNAL,
            or older style array control records, then `f` should be a file
            handle.  In this case ext_unit_dict is required, which can be
            constructed using the function
            :class:`flopy.utils.mfreadnam.parsenamefile`.

        Returns
        -------
        swr : ModflowSwr1 object
            ModflowSwr1 object (of type :class:`flopy.modflow.mfbas.ModflowSwr1`)

        Notes
        -----
        Load method still needs to be implemented.

        Examples
        --------

        >>> import flopy
        >>> m = flopy.modflow.Modflow()
        >>> swr = flopy.modflow.ModflowSwr1.load('test.swr', m)

        """

        if model.verbose:
            sys.stdout.write('loading swr1 process file...\n')

        # todo: everything

        openfile = not hasattr(f, 'read')
        if openfile:
            filename = f
            f = open(filename, 'r')

        print(
            'Warning: load method not completed. default swr1 object created.')

        if openfile:
            f.close()

        # determine specified unit number
        unitnumber = None
        filenames = [None]
        if ext_unit_dict is not None:
            unitnumber, filenames[0] = \
                model.get_ext_dict_attr(ext_unit_dict,
                                        filetype=ModflowSwr1.ftype())

        # create swr1 object instance
        swr1 = ModflowSwr1(model, unitnumber=unitnumber, filenames=filenames)

        # return swr object
        return swr1

    @staticmethod
    def ftype():
        return 'SWR'

    @staticmethod
    def defaultunit():
        return 36
