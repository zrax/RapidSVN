/*
 * ====================================================================
 * Copyright (c) 2000 The Apache Software Foundation.  All rights
 * reserved.
 *
 * This software is licensed as described in the file LICENSE.txt,
 * which you should have received as part of this distribution.
 *
 * This software consists of voluntary contributions made by many
 * individuals.  For exact contribution history, see the revision
 * history and logs, available at http://rapidsvn.tigris.org/.
 * ====================================================================
 */
#ifndef _MERGE_DLG_H_INCLUDED_
#define _MERGE_DLG_H_INCLUDED_

class MergeDlg:public wxDialog
{
public:
  struct sData 
  {
    sData();

    wxString Path1;
    wxString Path2;
    wxString Path1Rev;
    wxString Path2Rev;
    wxString Destination;
    wxString User;
    wxString Password;
    bool Recursive;
    bool Force;
  };
  
  MergeDlg (wxWindow *parent, sData* pData);
  void OnOK (wxCommandEvent& event);
  void OnBrowse (wxCommandEvent & event);

private:
  void InitializeData ();
  int TestRev (wxString & val);
  
  sData * m_pData;

  DECLARE_EVENT_TABLE ()
};

#endif
/* -----------------------------------------------------------------
 * local variables:
 * eval: (load-file "../rapidsvn-dev.el")
 * end:
 */