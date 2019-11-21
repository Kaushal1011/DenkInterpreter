package denkeditor;


import java.awt.Color;
import java.awt.Font;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JColorChooser;
import javax.swing.JFileChooser;
import javax.swing.JOptionPane;
import javax.swing.filechooser.FileNameExtensionFilter;
import org.apache.commons.io.FileUtils;
import org.fife.ui.rsyntaxtextarea.SyntaxConstants;
import say.swing.JFontChooser;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author KAUSHAL PATIL
 */
public class LightIde extends javax.swing.JFrame {

    /**
     * Creates new form LightIde
     */
    String curfilename;

    public LightIde() {

        initComponents();
        curfilename=null;
        codescroll.setLineNumbersEnabled(true);
        codescroll.setFoldIndicatorEnabled(true);
        
//        textArea = new RSyntaxTextArea(20, 60);
//      textArea.setSyntaxEditingStyle(SyntaxConstants.SYNTAX_STYLE_PYTHON);
//      textArea.setCodeFoldingEnabled(true);
//      sp = new RTextScrollPane(textArea);

//        unpack();
//      pack();
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jToggleButton1 = new javax.swing.JToggleButton();
        jScrollPane1 = new javax.swing.JScrollPane();
        jList1 = new javax.swing.JList<>();
        jPanel1 = new javax.swing.JPanel();
        codescroll = new org.fife.ui.rtextarea.RTextScrollPane();
        codearea = new org.fife.ui.rsyntaxtextarea.RSyntaxTextArea();
        jMenuBar1 = new javax.swing.JMenuBar();
        jMenu1 = new javax.swing.JMenu();
        jMenuItem1 = new javax.swing.JMenuItem();
        jMenuItem2 = new javax.swing.JMenuItem();
        Saveas = new javax.swing.JMenuItem();
        jMenuItem3 = new javax.swing.JMenuItem();
        jMenu3 = new javax.swing.JMenu();
        jMenuItem5 = new javax.swing.JMenuItem();
        jMenuItem6 = new javax.swing.JMenuItem();
        jMenu2 = new javax.swing.JMenu();
        jMenuItem4 = new javax.swing.JMenuItem();

        setDefaultCloseOperation(javax.swing.WindowConstants.DISPOSE_ON_CLOSE);
        setTitle("DenkEditor");

        jToggleButton1.setText("Select Language");
        jToggleButton1.setFocusable(false);
        jToggleButton1.setHorizontalTextPosition(javax.swing.SwingConstants.CENTER);
        jToggleButton1.setVerticalTextPosition(javax.swing.SwingConstants.BOTTOM);
        jToggleButton1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jToggleButton1ActionPerformed(evt);
            }
        });

        jList1.setModel(new javax.swing.AbstractListModel<String>() {
            String[] strings = { "Denk(Modified Pascal)", "Simple Text" };
            public int getSize() { return strings.length; }
            public String getElementAt(int i) { return strings[i]; }
        });
        jList1.addListSelectionListener(new javax.swing.event.ListSelectionListener() {
            public void valueChanged(javax.swing.event.ListSelectionEvent evt) {
                jList1ValueChanged(evt);
            }
        });
        jScrollPane1.setViewportView(jList1);

        codearea.setColumns(20);
        codearea.setRows(5);
        codescroll.setViewportView(codearea);

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addComponent(codescroll, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addContainerGap())
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addComponent(codescroll, javax.swing.GroupLayout.DEFAULT_SIZE, 605, Short.MAX_VALUE)
                .addContainerGap())
        );

        jMenu1.setText("File");

        jMenuItem1.setAccelerator(javax.swing.KeyStroke.getKeyStroke(java.awt.event.KeyEvent.VK_O, java.awt.event.InputEvent.CTRL_MASK));
        jMenuItem1.setText("Open");
        jMenuItem1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jMenuItem1ActionPerformed(evt);
            }
        });
        jMenu1.add(jMenuItem1);

        jMenuItem2.setAccelerator(javax.swing.KeyStroke.getKeyStroke(java.awt.event.KeyEvent.VK_S, java.awt.event.InputEvent.CTRL_MASK));
        jMenuItem2.setText("Save");
        jMenuItem2.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jMenuItem2ActionPerformed(evt);
            }
        });
        jMenu1.add(jMenuItem2);

        Saveas.setAccelerator(javax.swing.KeyStroke.getKeyStroke(java.awt.event.KeyEvent.VK_S, java.awt.event.InputEvent.SHIFT_MASK | java.awt.event.InputEvent.CTRL_MASK));
        Saveas.setText("Save As");
        Saveas.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                SaveasActionPerformed(evt);
            }
        });
        jMenu1.add(Saveas);

        jMenuItem3.setAccelerator(javax.swing.KeyStroke.getKeyStroke(java.awt.event.KeyEvent.VK_F4, java.awt.event.InputEvent.ALT_MASK));
        jMenuItem3.setText("Exit");
        jMenuItem3.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jMenuItem3ActionPerformed(evt);
            }
        });
        jMenu1.add(jMenuItem3);

        jMenuBar1.add(jMenu1);

        jMenu3.setText("Edit");

        jMenuItem5.setAccelerator(javax.swing.KeyStroke.getKeyStroke(java.awt.event.KeyEvent.VK_E, java.awt.event.InputEvent.CTRL_MASK));
        jMenuItem5.setText("Text Properties");
        jMenuItem5.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jMenuItem5ActionPerformed(evt);
            }
        });
        jMenu3.add(jMenuItem5);

        jMenuItem6.setAccelerator(javax.swing.KeyStroke.getKeyStroke(java.awt.event.KeyEvent.VK_E, java.awt.event.InputEvent.SHIFT_MASK | java.awt.event.InputEvent.CTRL_MASK));
        jMenuItem6.setText("Text Color");
        jMenuItem6.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jMenuItem6ActionPerformed(evt);
            }
        });
        jMenu3.add(jMenuItem6);

        jMenuBar1.add(jMenu3);

        jMenu2.setText("Run");
        jMenu2.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jMenu2ActionPerformed(evt);
            }
        });

        jMenuItem4.setAccelerator(javax.swing.KeyStroke.getKeyStroke(java.awt.event.KeyEvent.VK_F6, java.awt.event.InputEvent.SHIFT_MASK));
        jMenuItem4.setText("Run in CMD");
        jMenuItem4.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jMenuItem4ActionPerformed(evt);
            }
        });
        jMenu2.add(jMenuItem4);

        jMenuBar1.add(jMenu2);

        setJMenuBar(jMenuBar1);

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(10, 10, 10)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(jToggleButton1)
                        .addGap(26, 26, 26)
                        .addComponent(jScrollPane1, javax.swing.GroupLayout.DEFAULT_SIZE, 524, Short.MAX_VALUE)
                        .addContainerGap())
                    .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(10, 10, 10)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jToggleButton1, javax.swing.GroupLayout.PREFERRED_SIZE, 49, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 49, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(6, 6, 6)
                .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void jToggleButton1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jToggleButton1ActionPerformed
        // TODO add your handling code here:
        if (jList1.getSelectedIndex() == 0) {
            codearea.setSyntaxEditingStyle(SyntaxConstants.SYNTAX_STYLE_C);
            codearea.setCodeFoldingEnabled(true);

        }
        if (jList1.getSelectedIndex() == 1) {
            codearea.setSyntaxEditingStyle(SyntaxConstants.SYNTAX_STYLE_NONE);
            codearea.setCodeFoldingEnabled(true);

        }
//        if (jList1.getSelectedIndex() == 2) {
//            codearea.setSyntaxEditingStyle(SyntaxConstants.SYNTAX_STYLE_NONE);
//            codearea.setCodeFoldingEnabled(true);
//
//        }
//        if (jList1.getSelectedIndex() == 3) {
//            codearea.setSyntaxEditingStyle(SyntaxConstants.SYNTAX_STYLE_PYTHON);
//            codearea.setCodeFoldingEnabled(true);
//        }
//        if (jList1.getSelectedIndex() == 4) {
//            codearea.setSyntaxEditingStyle(SyntaxConstants.SYNTAX_STYLE_NONE);
//            codearea.setCodeFoldingEnabled(false);
//        }
    }//GEN-LAST:event_jToggleButton1ActionPerformed

    private void jMenuItem3ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jMenuItem3ActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_jMenuItem3ActionPerformed

    private void jMenuItem4ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jMenuItem4ActionPerformed
        // TODO add your handling code here:
//        curfilename="hello.c";
//curfilename="HelloWorld.java";
//curfilename="yo.py";
        if (curfilename == null) {
            JOptionPane.showMessageDialog(null, "Please Save File");

        } else {
            if (jList1.getSelectedIndex() == 0) {
                try {
                    // We are running "dir" and "ping" command on cmd 
                    Runtime.getRuntime().exec("cmd /c start cmd.exe /K " + "python " + "\"" +"src\\denkeditor\\interpreter.py" + "\"" + " "+"\"" + curfilename+"\"");
                    System.out.println("cmd /c start cmd.exe /K" + "python" + "\"" +"src\\denkeditor\\interpreter.py" + "\"" + " " + "\"" + curfilename+ "\"");
                } catch (IOException e) {
                    System.out.println("Cannot Open Cmd");
                }
            }
            if (jList1.getSelectedIndex() == 1) {
                System.out.println("Not runnable");
            }
//            if (jList1.getSelectedIndex() == 2) {
//                try {
//                    // We are running "dir" and "ping" command on cmd 
//                    String Javacname = curfilename.replace(".java", "");
//                    Runtime.getRuntime().exec("cmd /c start cmd.exe /K \"" + "java " + "\"" + curfilename + "\"");
////                    "&& java " + "\""+ Javacname + "\""+ "\"");
//                } catch (IOException e) {
//                    System.out.println("Cannot Open Cmd");
//                }
//            }
//            if (jList1.getSelectedIndex() == 3) {
//                try {
//                    // We are running "dir" and "ping" command on cmd 
//                    String Javacname = curfilename.replace(".java", "");
//                    Runtime.getRuntime().exec("cmd /c start cmd.exe /K \"" + "python " + "\"" + curfilename + "\"" + "\"");
//                } catch (IOException e) {
//                    System.out.println("Cannot Open Cmd");
//                }
//            }
        }
    }//GEN-LAST:event_jMenuItem4ActionPerformed

    private void jMenuItem1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jMenuItem1ActionPerformed
        // TODO add your handling code here:
        JFileChooser chooser = new JFileChooser();
        FileNameExtensionFilter filter = new FileNameExtensionFilter(
                ".C,.CPP,.PY,.JAVA,.PAS", "c", "cpp", "java", "py","pas");
        chooser.setFileFilter(filter);
        int returnVal = chooser.showOpenDialog(jPanel1);
        if (returnVal == JFileChooser.APPROVE_OPTION) {
            // System.out.println("You chose to open this file: " );
            File a = chooser.getSelectedFile();
//            String a;
            try {
                String content = FileUtils.readFileToString(a, StandardCharsets.UTF_8);
                codearea.setText(content);
                curfilename = a.getAbsolutePath();
//                a.getName();
//                curfilename.replace("\\","\\\\");
            } catch (IOException ex) {
//                Logger.getLogger(SwingP.class.getName()).log(Level.SEVERE, null, ex);
                JOptionPane.showMessageDialog(null, ex.getMessage());
            }

        }


    }//GEN-LAST:event_jMenuItem1ActionPerformed

    private void SaveasActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_SaveasActionPerformed
        // TODO add your handling code here:
         FileNameExtensionFilter pngFilter = new FileNameExtensionFilter("Code Files or Text Files", "txt","c","cpp","py","java","pas");
        // add filters
        JFileChooser chooser1=new JFileChooser();
        chooser1.addChoosableFileFilter(pngFilter);
        chooser1.setFileFilter(pngFilter);
        int returnVal = chooser1.showSaveDialog(Saveas);
        if (returnVal == JFileChooser.APPROVE_OPTION) {
            // System.out.println("You chose to open this file: " );

//            BufferedImage img = null;
            File aa = chooser1.getSelectedFile();
            curfilename=aa.getAbsolutePath();
            File file = new File(aa.getAbsolutePath());
            FileWriter fr = null;
            try {
                fr = new FileWriter(file);
                fr.write(codearea.getText());
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
                //close resources
                try {
                    fr.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }//GEN-LAST:event_SaveasActionPerformed

    private void jMenuItem2ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jMenuItem2ActionPerformed
        // TODO add your handling code here:
        if (curfilename == null) {
            Saveas.doClick();
        } else {
            File file = new File(curfilename);
            FileWriter fr = null;
            try {
                fr = new FileWriter(file);
                fr.write(codearea.getText());
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
                //close resources
                try {
                    fr.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }//GEN-LAST:event_jMenuItem2ActionPerformed

    private void jMenuItem5ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jMenuItem5ActionPerformed
        // TODO add your handling code here:
        JFontChooser fontChooser = new JFontChooser();
			fontChooser.setSelectedFont(codearea.getFont());
			int result = fontChooser.showDialog(null);
			if (result == JFontChooser.OK_OPTION) {
				Font font = fontChooser.getSelectedFont();
				//LOG.info("Selected Font : {}", font);
				codearea.setFont(font);
				
			}
        
        
        
        
    }//GEN-LAST:event_jMenuItem5ActionPerformed

    private void jMenuItem6ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jMenuItem6ActionPerformed
        // TODO add your handling code here:
        codearea.setForeground(JColorChooser.showDialog(rootPane, curfilename, Color.yellow));
        
    }//GEN-LAST:event_jMenuItem6ActionPerformed

    private void jList1ValueChanged(javax.swing.event.ListSelectionEvent evt) {//GEN-FIRST:event_jList1ValueChanged
        // TODO add your handling code here:
    }//GEN-LAST:event_jList1ValueChanged

    private void jMenu2ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jMenu2ActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_jMenu2ActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(LightIde.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(LightIde.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(LightIde.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(LightIde.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new LightIde().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JMenuItem Saveas;
    public org.fife.ui.rsyntaxtextarea.RSyntaxTextArea codearea;
    public org.fife.ui.rtextarea.RTextScrollPane codescroll;
    public javax.swing.JList<String> jList1;
    private javax.swing.JMenu jMenu1;
    private javax.swing.JMenu jMenu2;
    private javax.swing.JMenu jMenu3;
    private javax.swing.JMenuBar jMenuBar1;
    private javax.swing.JMenuItem jMenuItem1;
    private javax.swing.JMenuItem jMenuItem2;
    private javax.swing.JMenuItem jMenuItem3;
    private javax.swing.JMenuItem jMenuItem4;
    private javax.swing.JMenuItem jMenuItem5;
    private javax.swing.JMenuItem jMenuItem6;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JToggleButton jToggleButton1;
    // End of variables declaration//GEN-END:variables
}